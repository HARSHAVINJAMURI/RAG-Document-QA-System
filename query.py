import faiss
import pickle
import os
from sentence_transformers import SentenceTransformer
from groq import Groq

VECTOR_PATH = "vectorstore/faiss_index"
CHUNKS_PATH = "vectorstore/chunks.pkl"

embedder = SentenceTransformer("all-MiniLM-L6-v2")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# client = Groq(api_key="YOUR_GROQ_API_KEY")
def ask_question(question: str) -> str:
    # ---- Safety check ----
    if not os.path.exists(VECTOR_PATH) or not os.path.exists(CHUNKS_PATH):
        return "No document indexed yet. Please upload a document first."

    # ---- Load index dynamically ----
    index = faiss.read_index(VECTOR_PATH)
    with open(CHUNKS_PATH, "rb") as f:
        chunks = pickle.load(f)

    # ---- Retrieval ----
    q_embedding = embedder.encode([question])
    _, indices = index.search(q_embedding, k=8)

    context = "\n\n".join(chunks[i] for i in indices[0])

    # ---- Prompt ----
    prompt = f"""
You are an expert document analysis assistant.

Tasks:
1. Identify the document type (resume, report, article, etc).
2. Answer the question strictly using the context.
3. If the answer is not present, say "Not found in the document".

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
    )

    return response.choices[0].message.content.strip()
