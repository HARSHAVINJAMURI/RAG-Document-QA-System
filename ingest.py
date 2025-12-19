# from sentence_transformers import SentenceTransformer
# import faiss
# import os
# from pypdf import PdfReader
# import pickle

# model = SentenceTransformer("all-MiniLM-L6-v2")

# def load_pdf(path):
#     reader = PdfReader(path)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text()
#     return text

# def chunk_text(text, size=500):
#     return [text[i:i+size] for i in range(0, len(text), size)]

# text = load_pdf("data/sample.pdf")
# chunks = chunk_text(text)

# embeddings = model.encode(chunks)

# index = faiss.IndexFlatL2(len(embeddings[0]))
# index.add(embeddings)

# os.makedirs("vectorstore", exist_ok=True)
# faiss.write_index(index, "vectorstore/faiss_index")

# with open("vectorstore/chunks.pkl", "wb") as f:
#     pickle.dump(chunks, f)

# print("Documents indexed successfully")


import os
import faiss
import pickle
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

# ---------- Embedding Model ----------
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# ---------- Load PDF ----------
def load_pdf(path: str) -> str:
    reader = PdfReader(path)
    pages_text = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages_text.append(text)

    return "\n".join(pages_text).strip()

# ---------- Chunking ----------
# def chunk_text(text: str, chunk_size: int = 400, overlap: int = 50):
#     chunks = []
#     start = 0

#     while start < len(text):
#         end = start + chunk_size
#         chunks.append(text[start:end])
#         start = end - overlap

#     return chunks
def chunk_text(text):
    sections = text.split("\n\n")
    chunks = []
    current_chunk = ""

    for section in sections:
        if len(current_chunk) + len(section) < 800:
            current_chunk += section + "\n\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = section + "\n\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

# ---------- Ingest Document ----------
def ingest_document(pdf_path: str):
    text = load_pdf(pdf_path)

    if not text:
        raise ValueError("Uploaded PDF contains no readable text.")

    chunks = chunk_text(text)

    # Safety check
    if len(chunks) == 0:
        raise ValueError("No text chunks created from document.")

    embeddings = embedder.encode(chunks, show_progress_bar=False)

    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # Save vector store
    os.makedirs("vectorstore", exist_ok=True)
    faiss.write_index(index, "vectorstore/faiss_index")

    with open("vectorstore/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    return {
        "chunks": len(chunks),
        "status": "Document indexed successfully"
    }
