from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from .db import collection

embeddings = OpenAIEmbeddings()

def ingest_pdf(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    for doc in docs:
        content = doc.page_content
        vector = embeddings.embed_query(content)
        collection.add(documents=[content], embeddings=[vector])