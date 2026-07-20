"""
Semantic Retriever

This module converts a user query into an embedding,
searches the FAISS vector database,
and returns the most relevant chunks.
"""

from rag.embedding_model import EmbeddingModel
from rag.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

        self.vector_store = VectorStore()

        self.vector_store.load()

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ):

        query_embedding = self.embedding_model.embed_text(
            query
        )

        results = self.vector_store.search(
            query_embedding,
            top_k
        )

        return results