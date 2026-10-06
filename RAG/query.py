from openai import OpenAI
import chromadb
from dotenv import load_dotenv

load_dotenv(override=True)

client = OpenAI()

chroma_client = chromadb.PersistentClient(
    path="RAG/chroma_db"
)

collection = chroma_client.get_collection(
    name="documents"
)

question = input("Question: ")

# 1. Convert question into embedding
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=question
)

query_embedding = response.data[0].embedding

# 2. Search ChromaDB
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

# 3. Get retrieved chunks
documents = results["documents"][0]

context = "\n\n".join(documents)

# 4. Ask LLM to answer using the retrieved context
prompt = f"""
Answer the question using only the relevant information from the context.

Give a concise answer focused specifically on the question.
Do not repeat the entire context.

Context:
{context}

Question:
{question}
"""

# 5. Generate final answer
response = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\n---")
print(response.choices[0].message.content)