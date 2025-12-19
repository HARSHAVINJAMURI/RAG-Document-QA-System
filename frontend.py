import streamlit as st
import os
from ingest import ingest_document
from query import ask_question

st.set_page_config(page_title="RAG Document Q&A", layout="centered")

st.title("📄 RAG-Based Document Q&A System")

# Upload section
st.header("Upload Document")
uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file:
    os.makedirs("uploads", exist_ok=True)
    file_path = os.path.join("uploads", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Indexing document..."):
        ingest_document(file_path)

    st.success("Document indexed successfully")

# Question section
st.header("Ask a Question")
question = st.text_input("Enter your question")

if st.button("Get Answer"):
    if not question:
        st.warning("Please enter a question")
    else:
        with st.spinner("Generating answer..."):
            answer = ask_question(question)

        st.subheader("Answer")
        st.write(answer)
