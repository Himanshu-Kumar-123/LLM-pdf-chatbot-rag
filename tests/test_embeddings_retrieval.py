from ingestion.pdf_loader import load_pdf
from ingestion.chunker import chunk_text
from embeddings.embedder import embed_texts
from embeddings.vector_store import build_faiss_index
from retrieval.retriever import retrieve_top_k

# Load and chunk
text = load_pdf("data/sample_doc.pdf")
chunks = chunk_text(text)

# Embed chunks
chunk_embeddings = embed_texts(chunks)

# Build FAISS index
index = build_faiss_index(chunk_embeddings)

# Test query
query = "What is this document about?"
query_embedding = embed_texts([query])

# Retrieve
results = retrieve_top_k(query_embedding, index, chunks, k=3)

print("\n--- Retrieved Chunks ---\n")
for i, r in enumerate(results, 1):
    print(f"\nResult {i}:\n{r[:300]}")