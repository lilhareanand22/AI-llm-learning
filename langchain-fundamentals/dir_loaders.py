from langchain_community.document_loaders import (
    TextLoader,
    DirectoryLoader,
    PyPDFLoader,
    CSVLoader
)
from pathlib import Path

data_directory = Path(__file__).resolve().parent / "data"
dir_loader = DirectoryLoader(
    str(data_directory),
    glob="**/*.txt",
    loader_cls=TextLoader,
)
dir_documents = dir_loader.load()

print("Directory Text Documents:", dir_documents)