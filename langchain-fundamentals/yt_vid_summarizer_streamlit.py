import os
from urllib.parse import urlparse

import streamlit as st
from dotenv import load_dotenv

from yt_vid_summarizer import YoutubeVideoSummarizer

load_dotenv()

LLM_MODELS = {
    "OpenAI": {
        "type": "openai",
        "models": ["gpt-4o-mini", "gpt-4o"],
    },
    "Ollama": {
        "type": "ollama",
        "models": ["llama3.2", "mistral"],
    },
}

EMBEDDING_MODELS = {
    "OpenAI (text-embedding-3-small)": "openai",
    "Nomic Embed Text (Ollama)": "nomic",
}


def is_youtube_url(url: str) -> bool:
    parsed = urlparse(url)
    hostname = (parsed.hostname or "").lower()
    return parsed.scheme in {"http", "https"} and hostname in {
        "youtube.com",
        "www.youtube.com",
        "m.youtube.com",
        "youtu.be",
        "www.youtu.be",
    }


def main() -> None:
    st.set_page_config(page_title="YouTube video summarizer")
    st.title("YouTube video summarizer")
    st.write("Summarize a video's transcript and ask questions about its content.")

    st.session_state.setdefault("video_result", None)
    st.session_state.setdefault("chat_history", [])
    st.session_state.setdefault("active_models", None)

    with st.sidebar:
        st.header("Model selection")
        provider = st.selectbox("LLM provider", list(LLM_MODELS))
        model_name = st.selectbox("LLM model", LLM_MODELS[provider]["models"])
        embedding_label = st.selectbox(
            "Embedding model", list(EMBEDDING_MODELS)
        )

        uses_openai = (
            provider == "OpenAI"
            or EMBEDDING_MODELS[embedding_label] == "openai"
        )
        if uses_openai and not os.getenv("OPENAI_API_KEY"):
            st.info("Add OPENAI_API_KEY to your .env file to use OpenAI models.")
        if provider == "Ollama" or embedding_label.startswith("Nomic"):
            st.caption(
                "Ollama must be running locally, with the selected model installed."
            )

    with st.form("video_form"):
        video_url = st.text_input(
            "YouTube video URL",
            placeholder="https://www.youtube.com/watch?v=...",
        )
        process_video = st.form_submit_button(
            "Summarize video",
            type="primary",
            icon=":material/summarize:",
        )

    if process_video:
        st.session_state.video_result = None
        st.session_state.chat_history = []

        if not is_youtube_url(video_url.strip()):
            st.error("Enter a valid YouTube URL starting with http:// or https://.")
        elif uses_openai and not os.getenv("OPENAI_API_KEY"):
            st.error("OPENAI_API_KEY is not set. Add it to your .env file and restart.")
        else:
            active_models = {
                "llm_type": LLM_MODELS[provider]["type"],
                "llm_model_name": model_name,
                "embedding_type": EMBEDDING_MODELS[embedding_label],
            }
            try:
                with st.spinner(
                    "Downloading the video, transcribing audio, and creating a summary..."
                ):
                    summarizer = YoutubeVideoSummarizer(**active_models)
                    result = summarizer.process_video(video_url.strip())

                st.session_state.video_result = result
                st.session_state.active_models = active_models
            except Exception as error:
                st.error(f"Could not process this video: {error}")

    result = st.session_state.video_result
    if result:
        st.subheader(result["title"])
        active_models = st.session_state.active_models
        st.caption(
            f"LLM: {active_models['llm_type']} / {active_models['llm_model_name']} "
            f"| Embeddings: {active_models['embedding_type']}"
        )

        with st.container(border=True):
            st.markdown("### Summary")
            st.markdown(result["summary"])

        with st.expander("View full transcript"):
            st.text(result["full_transcript"])

        st.divider()
        st.subheader("Ask questions about the video")

        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        question = st.chat_input("Ask a question about this video")
        if question:
            st.session_state.chat_history.append(
                {"role": "user", "content": question}
            )
            with st.chat_message("user"):
                st.markdown(question)

            try:
                with st.spinner("Searching the transcript..."):
                    response = result["qa_chain"].invoke({"question": question})
                answer = response["answer"]
                st.session_state.chat_history.append(
                    {"role": "assistant", "content": answer}
                )
                with st.chat_message("assistant"):
                    st.markdown(answer)
            except Exception as error:
                st.error(f"Could not answer the question: {error}")


if __name__ == "__main__":
    main()
