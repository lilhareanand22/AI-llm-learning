from langchain_community.document_loaders import (
    PyPDFLoader,
)
from pathlib import Path

pdf_path = Path(__file__).resolve().parent / "doc" / "linux-manual.pdf"
pdf_loader = PyPDFLoader(str(pdf_path))

docs = pdf_loader.load()
print("PDF Documents:", docs)