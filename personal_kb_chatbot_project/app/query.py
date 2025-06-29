from langchain.embeddings import OpenAIEmbeddings
from .db import collection

embeddings = OpenAIEmbeddings()

def query_knowledge_base(query_text):
    query_vec = embeddings.embed_query(query_text)
    results = collection.query(query_embeddings=[query_vec], n_results=3)
    return results["documents"]