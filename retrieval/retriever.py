def retrieve_top_k(query_embedding, index, chunks, k=3):
    """
    Retrieves top-k most similar chunks
    """
    distances, indices = index.search(query_embedding, k)
    return [chunks[i] for i in indices[0]]