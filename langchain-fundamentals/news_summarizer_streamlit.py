import os
from urllib.parse import urlparse

import streamlit as st
from dotenv import load_dotenv
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_text_splitters import RecursiveCharacterTextSplitter
from newspaper import Article

load_dotenv()


class NewsArticleSummarizer:
    def __init__(
        self,
        model_type: str,
        model_name: str,
    ):
        self.model_type = model_type
        self.model_name = model_name

        if model_type == "OpenAI":
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError(
                    "OPENAI_API_KEY is not set. Add it to your .env file to use OpenAI."
                )
            self.llm = ChatOpenAI(model=model_name, api_key=api_key)
        elif model_type == "Ollama":
            self.llm = ChatOllama(model=model_name, temperature=0, timeout=120)
        else:
            raise ValueError(f"Unsupported model provider: {model_type}")

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200,
            length_function=len,
        )

    def fetch_article(self, url: str) -> Article:
        article = Article(url)
        article.download()
        article.parse()

        if not article.text.strip():
            raise ValueError(
                "No article text was found at that URL. Check the link or try another article."
            )
        return article

    def create_documents(self, article: Article) -> list[Document]:
        chunks = self.text_splitter.split_text(article.text)
        return [
            Document(
                page_content=chunk,
                metadata={"source": article.url, "title": article.title},
            )
            for chunk in chunks
        ]

    def summarize(self, url: str, summary_type: str) -> dict:
        article = self.fetch_article(url)
        documents = self.create_documents(article)

        if summary_type == "Detailed":
            map_prompt_template = (
                'Write a detailed summary of the following text:\n"{text}"\n'
                "DETAILED SUMMARY:"
            )
            combine_prompt_template = (
                "Write a detailed summary combining the previous summaries:\n"
                '"{text}"\nFINAL DETAILED SUMMARY:'
            )
        else:
            map_prompt_template = (
                'Write a concise summary of the following text:\n"{text}"\n'
                "CONCISE SUMMARY:"
            )
            combine_prompt_template = (
                "Write a concise summary combining the previous summaries:\n"
                '"{text}"\nFINAL CONCISE SUMMARY:'
            )

        chain = load_summarize_chain(
            llm=self.llm,
            chain_type="map_reduce",
            map_prompt=PromptTemplate(
                template=map_prompt_template,
                input_variables=["text"],
            ),
            combine_prompt=PromptTemplate(
                template=combine_prompt_template,
                input_variables=["text"],
            ),
        )
        result = chain.invoke({"input_documents": documents})

        return {
            "title": article.title or "Untitled article",
            "authors": article.authors,
            "publish_date": article.publish_date,
            "summary": result["output_text"],
            "url": url,
            "model_type": self.model_type,
            "model_name": self.model_name,
        }


def is_valid_http_url(url: str) -> bool:
    parsed_url = urlparse(url)
    return parsed_url.scheme in {"http", "https"} and bool(parsed_url.netloc)


def main() -> None:
    st.set_page_config(page_title="News article summarizer")
    st.title("News article summarizer")
    st.write("Summarize a news article using an OpenAI or Ollama chat model.")

    with st.sidebar:
        st.header("LLM model")
        model_type = st.selectbox("Provider", ["OpenAI", "Ollama"])

        if model_type == "OpenAI":
            model_name = st.selectbox("Model", ["gpt-4o-mini", "gpt-4o"])
            if not os.getenv("OPENAI_API_KEY"):
                st.info("Set OPENAI_API_KEY in your .env file to use OpenAI.")
        else:
            model_name = st.selectbox("Model", ["llama3.2", "mistral"])
            st.caption("Make sure Ollama is running and the selected model is installed.")

    with st.form("article_summary_form"):
        url = st.text_input(
            "Article URL",
            placeholder="https://example.com/news/article",
        )
        summary_type = st.selectbox("Summary length", ["Detailed", "Concise"])
        submitted = st.form_submit_button(
            "Summarize article",
            type="primary",
            icon=":material/summarize:",
        )

    if submitted:
        if not is_valid_http_url(url.strip()):
            st.error("Enter a valid article URL starting with http:// or https://.")
            st.session_state.pop("summary_result", None)
        else:
            try:
                summarizer = NewsArticleSummarizer(
                    model_type=model_type,
                    model_name=model_name,
                )
                with st.spinner("Fetching and summarizing the article..."):
                    st.session_state.summary_result = summarizer.summarize(
                        url.strip(),
                        summary_type,
                    )
            except Exception as error:
                st.session_state.pop("summary_result", None)
                st.error(f"Could not summarize this article: {error}")

    result = st.session_state.get("summary_result")
    if result:
        st.divider()
        st.subheader(result["title"])
        st.caption(
            f"Model: {result['model_type']} / {result['model_name']}  |  "
            f"Source: {result['url']}"
        )
        if result["authors"]:
            st.caption(f"Author(s): {', '.join(result['authors'])}")
        if result["publish_date"]:
            publish_date = result["publish_date"]
            if hasattr(publish_date, "strftime"):
                publish_date = publish_date.strftime("%B %d, %Y")
            st.caption(f"Published: {publish_date}")
        st.markdown(result["summary"])


if __name__ == "__main__":
    main()
