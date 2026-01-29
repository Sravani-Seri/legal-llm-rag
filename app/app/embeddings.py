from typing import List
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

def get_embeddings(texts: List[str]) -> List[List[float]]:
    """
    Generate embeddings for a list of texts using OpenAI Embeddings API.
    Returns a list of embedding vectors.
    """
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    embeddings = [item.embedding for item in response.data]
    return embeddings

if __name__ == "__main__":
    sample_texts = ["This is a sample legal document.", "Another piece of text."]
    print(get_embeddings(sample_texts))
