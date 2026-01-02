# 📄 Chatbot over PDFs using Retrieval-Augmented Generation (RAG)

## 🔍 Overview
This project implements a **Retrieval-Augmented Generation (RAG)** based chatbot that allows users to upload PDF documents and ask questions in natural language.

The chatbot generates answers **strictly grounded in the content of the uploaded PDFs**, reducing hallucinations commonly observed in standalone language models.

---

## 🧠 Key Idea
Instead of training a language model on PDFs, the system follows a retrieval-based approach:

- Extract and clean text from PDFs  
- Split text into overlapping chunks  
- Convert chunks into dense vector embeddings  
- Store embeddings in a vector database  
- Retrieve relevant chunks at query time  
- Generate answers using an LLM **only from retrieved context**

> **Important:**  
> The language model itself is **not trained on PDFs**.

---

## 🏗️ Architecture

PDF → Text Extraction → Chunking → Embeddings → Vector Database
↑
User Query → Embedding → Retrieval → Context → LLM → Answer


---

## 🛠️ Tech Stack

- **Language:** Python  
- **UI:** Streamlit  
- **Embeddings:** Sentence Transformers  
- **Vector Store:** FAISS  
- **LLM (Local Development):** Ollama (Mistral)

> Ollama is used during local development to avoid API costs and quota limits.  
> The LLM backend can be replaced with a hosted model (e.g., OpenAI) during deployment.

---

## 🚀 How to Run Locally

### 1️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate

2️⃣ Install dependencies
pip install -r requirements.txt