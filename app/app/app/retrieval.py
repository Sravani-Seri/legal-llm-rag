from typing import List, Tuple
import faiss
import numpy as np

class VectorStore:
    def __init__(self, dimension: int):
        """
        Initialize FAISS vector store.
        """
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.texts = []

    def add_vectors(self, embeddings: List[List[float]], texts: List[str]):
        """
        Add embeddings and their corresponding texts to the store.
        """
        vectors = np.array(embeddings).astype('float32')
        self.index.add(vectors)
        self.texts.extend(texts)

    def search(self, query_embedding: List[float], top_k: int = 3) -> List[Tuple[str, float]]:
        """
        Search the vector store for the top_k closest vectors to the query embedding.
        Returns a list of (text, distance) tuples.
        """
        query_vector = np.array([query_embedding]).astype('float32')
        distances, indices = self.index.search(query_vector, top_k)
        results = [(self.texts[i], distances[0][idx]) for idx, i in enumerate(indices[0])]
        return results

if __name__ == "__main__":
    # Example usage
    store = VectorStore(dimension=1536)  # dimension matches OpenAI text-embedding-3-small
    dummy_embeddings = np.random.rand(2, 1536).tolist()
    dummy_texts = ["Doc 1 text", "Doc 2 text"]
    store.add_vectors(dummy_embeddings, dummy_texts)
    query = np.random.rand(1536).tolist()
    print(store.search(query))
