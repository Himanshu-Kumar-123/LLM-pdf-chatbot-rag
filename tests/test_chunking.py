from ingestion.pdf_loader import load_pdf
from ingestion.chunker import chunk_text

text = load_pdf("data/sample_doc.pdf")
chunks = chunk_text(text)

print(f"Total chunks: {len(chunks)}")
print("\n--- SAMPLE CHUNK ---\n")
print(chunks[0])