import streamlit as st

from ingestion.pdf_loader import load_pdf
from ingestion.chunker import chunk_text
from embeddings.embedder import embed_texts
from embeddings.vector_store import build_faiss_index
from retrieval.retriever import retrieve_top_k
from llm.generator import generate_answer

# ---------------- UI SETUP ----------------
st.set_page_config(page_title="PDF Chatbot (RAG)", layout="centered")
st.title("📄 Chatbot over PDFs")
st.caption("Ask questions grounded only in the uploaded PDF")

# ---------------- SESSION STATE ----------------
if "index" not in st.session_state:
    st.session_state.index = None
    st.session_state.chunks = None

# ---------------- PDF UPLOAD ----------------
pdf = st.file_uploader("Upload a PDF", type=["pdf"])

if pdf and st.session_state.index is None:
    with st.spinner("Processing PDF..."):
        text = load_pdf(pdf)
        chunks = chunk_text(text)
        embeddings = embed_texts(chunks)
        index = build_faiss_index(embeddings)

        st.session_state.index = index
        st.session_state.chunks = chunks

    st.success("PDF processed successfully! You can now ask questions.")

# ---------------- QUESTION INPUT ----------------
question = st.text_input("Ask a question about the document")

if question and st.session_state.index:
    with st.spinner("Thinking..."):
        query_embedding = embed_texts([question])
        retrieved_chunks = retrieve_top_k(
            query_embedding,
            st.session_state.index,
            st.session_state.chunks,
            k=5
        )

        context = "\n\n".join(retrieved_chunks)
        answer = generate_answer(context, question)

    st.subheader("Answer")
    st.write(answer)

    with st.expander("🔍 Retrieved Context (Debug)"):
        st.write(context)