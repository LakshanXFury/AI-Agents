This is the Basic RAG for this project, not using langraphs chunk splitter : RecursiveCharacterTextSplitter. 

Chroma will find the chunks whose meaning is most similar to your question.


Document
   ↓
Chunks
   ↓
Embeddings
   ↓
Chroma
   ↓
Similarity Search
   ↓
Relevant chunks

**FLOW DIAGRAM**

                    ┌─────────────────────┐
                    │   sampl.txt         │
                    │                     │
                    │ LangGraph is...     │
                    │ Nodes perform...    │
                    │ Edges determine...  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     ingest.py       │
                    │                     │
                    │ Read document       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Chunking       │
                    │                     │
                    │ Split into 500      │
                    │ character chunks    │
                    └──────────┬──────────┘
                               │
                               ▼
              ┌─────────────────────────────────┐
              │       Create Embeddings         │
              │                                 │
              │ text-embedding-3-small          │
              │                                 │
              │ Text → Numbers (Vector)         │
              └───────────────┬─────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │      ChromaDB       │
                    │                     │
                    │ Chunk + Embedding   │
                    │ stored locally      │
                    └──────────┬──────────┘
                               │
                               │
                 ──────────────┼──────────────
                               │
                               ▼
                    ┌─────────────────────┐
                    │      User Query     │
                    │                     │
                    │ "What is a node     │
                    │  in LangGraph?"     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Create Query        │
                    │ Embedding           │
                    │                     │
                    │ Question → Vector   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      ChromaDB       │
                    │                     │
                    │ Similarity Search   │
                    │                     │
                    │ Find relevant       │
                    │ chunks              │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Retrieved Context   │
                    │                     │
                    │ "Nodes perform      │
                    │  actions..."        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │        LLM          │
                    │                     │
                    │ Question + Context  │
                    │        ↓            │
                    │ Generate Answer     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Final Answer     │
                    │                     │
                    │ "A node in          │
                    │ LangGraph is a      │
                    │ unit that performs  │
                    │ an action..."       │
                    └─────────────────────┘

**Phase 1 — Ingestion**

Document
   ↓
Chunks
   ↓
Embeddings
   ↓
ChromaDB

**Phase 2 — Query**

Question
   ↓
Question Embedding
   ↓
ChromaDB Search
   ↓
Relevant Chunks
   ↓
LLM
   ↓
Answer