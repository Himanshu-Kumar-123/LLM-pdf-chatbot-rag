from ingestion.pdf_loader import load_pdf
from ingestion.chunker import chunk_text
from embeddings.embedder import embed_texts
from embeddings.vector_store import build_faiss_index
from retrieval.retriever import retrieve_top_k
from llm.generator import generate_answer

# Load PDF
text = load_pdf("data/sample_doc.pdf")
chunks = chunk_text(text)

# Embed + index
embeddings = embed_texts(chunks)
index = build_faiss_index(embeddings)

# Ask a question
question = "What is this document about?"
#question = "What is spam filer?"
#question = "What is Machine Learning according to Arthur Samuel?"

# Retrieve context
query_embedding = embed_texts([question])
retrieved_chunks = retrieve_top_k(query_embedding, index, chunks, k=3)
context = "\n\n".join(retrieved_chunks)

# Generate answer
answer = generate_answer(context, question)

print("\n--- ANSWER ---\n")
print(answer)