from chromadb import Client

client = Client()
collection = client.create_collection("kb")