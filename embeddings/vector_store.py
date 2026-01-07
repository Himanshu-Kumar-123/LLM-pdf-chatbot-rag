import faiss
import numpy as np

def build_faiss_index(embeddings):
    """
    Builds a FAISS index from embeddings
    """
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)  # L2 distance
    index.add(np.array(embeddings))
    return index