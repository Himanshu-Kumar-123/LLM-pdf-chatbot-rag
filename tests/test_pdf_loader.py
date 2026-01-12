from ingestion.pdf_loader import load_pdf

text = load_pdf("data/sample_doc.pdf")
print(text[:1000])  # print first 1000 characters