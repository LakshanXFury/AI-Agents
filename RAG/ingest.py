from openai import OpenAI
import chromadb
from dotenv import load_dotenv

load_dotenv(override=True)

client = OpenAI()

chroma_client = chromadb.PersistentClient(
    path="RAG/chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="documents"
)

with open("RAG/documents/sampl.txt", "r") as f:
    text = f.read()

# Simple chunking for learning
chunk_size = 500

chunks = [
    text[i:i + chunk_size]
    for i in range(0, len(text), chunk_size)
]

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=chunks
)

embeddings = [
    item.embedding
    for item in response.data
]

collection.add(
    ids=[f"chunk_{i}" for i in range(len(chunks))],
    documents=chunks,
    embeddings=embeddings
)

print(f"Stored {len(chunks)} chunks.")