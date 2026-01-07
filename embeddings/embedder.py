from sentence_transformers import SentenceTransformer

# Small, fast, interview-friendly model
_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts):
    """
    Converts list of text chunks into embeddings
    """
    return _model.encode(texts, show_progress_bar=False)