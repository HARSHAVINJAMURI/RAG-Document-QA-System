# RAG-Document-QA-System

## Overview
This project is a **Retrieval-Augmented Generation (RAG) based Document Question Answering system** that allows users to upload documents (such as resumes or text-based PDFs) and ask natural language questions about their content. The system retrieves the most relevant document chunks using vector similarity search and generates accurate, grounded answers using a Large Language Model (LLM).

The application is designed to be **lightweight, scalable, secure, and production-ready**, using free-tier-friendly tools and deployed as a web application using Streamlit.

---

## Author
**Harsha Vinjamuri**  
Rajahmundry, Andhra Pradesh, India  

- Portfolio: https://harshavinjamuri.framer.ai/  
- GitHub: https://github.com/harshavinjamuri  
- LinkedIn: https://linkedin.com/in/harshavinjamuri  
- Email: vinjamuriharsha123@gmail.com  

---

## Key Features
- Upload PDF documents dynamically
- Semantic document chunking for better retrieval
- Vector-based similarity search using FAISS
- Accurate, context-grounded answers using LLMs
- Resume-aware and structured document parsing
- Token-efficient prompt design for free-tier APIs
- Secure API key handling using environment variables and Streamlit Secrets
- Fully deployed on Streamlit Cloud

---

## System Architecture
1. User uploads a document via Streamlit UI  
2. Document text is extracted and semantically chunked  
3. Chunks are converted into embeddings using Sentence Transformers  
4. FAISS stores and retrieves the most relevant chunks  
5. Retrieved context is compressed and passed to the LLM  
6. The LLM generates an accurate answer strictly based on the document  

---

## Tech Stack
**Frontend**
- Streamlit

**Backend / Core Logic**
- Python
- FAISS (Vector Database)
- Sentence-Transformers (Embeddings)

**LLM**
- Groq API (LLaMA 3.1 – Free Tier)

**Document Processing**
- PyPDF

**Deployment**
- Streamlit Community Cloud

---

## Why RAG?
Traditional LLMs hallucinate when asked about private documents.  
RAG solves this by:
- Retrieving only relevant document context
- Grounding LLM responses in real data
- Improving accuracy and trustworthiness

This project demonstrates a **production-grade RAG workflow** suitable for enterprise document search, resume parsing, and internal knowledge bases.

---

## Installation (Local Setup)

```bash
git clone https://github.com/harshavinjamuri/rag-doc-qa.git
cd rag-doc-qa
pip install -r requirements.txt
streamlit run frontend.py
```
---

## Environment Variables

The application uses secure environment variables for API keys.

### Local (Windows PowerShell)

```powershell
setx GROQ_API_KEY "your_groq_api_key"
```

### Streamlit Cloud

Add the following in **App Settings → Secrets**:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

---

## Project Structure

```
rag-doc-qa/
│
├── frontend.py        # Streamlit UI
├── query.py           # RAG query logic
├── ingest.py          # Document ingestion & indexing
├── requirements.txt
├── uploads/           # Temporary uploaded files
└── vectorstore/       # FAISS index (runtime)
```

---

## Example Use Cases

* Resume parsing and analysis
* Academic paper Q&A
* Internal company document chatbot
* Knowledge base search
* Portfolio-level AI project demonstration

---

## Key Engineering Decisions

* Semantic chunking instead of fixed-size chunking
* High-recall retrieval with controlled context compression
* Prompt design optimized for structured extraction
* Token-efficient LLM calls to avoid free-tier limits
* Secure secret management (no hardcoded keys)

---

## Challenges Solved

* Hallucinations from weak local models
* Token limit errors with free-tier APIs
* Resume section fragmentation
* GPU / CUDA dependency issues
* Secure deployment without exposing API keys

---

## Future Enhancements

* Multi-document knowledge base
* Chat-style multi-turn conversation
* Source citation highlighting
* Authentication and user history
* Support for DOCX and TXT files

---

## Conclusion

This project represents a **complete, real-world RAG implementation** built with practical constraints in mind. It demonstrates strong understanding of document retrieval, LLM integration, prompt engineering, and cloud deployment — making it suitable for both production use and portfolio presentation.

---

## License

This project is open-source and intended for educational and portfolio use.

---

**Developed and maintained by Harsha Vinjamuri**
Portfolio: [https://harshavinjamuri.framer.ai/](https://harshavinjamuri.framer.ai/)

