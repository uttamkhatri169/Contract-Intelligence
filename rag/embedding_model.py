from sentence_transformers import SentenceTransformer

from rag.config import EMBEDDING_MODEL


class EmbeddingModel:
    """
    Wrapper around SentenceTransformer.
    Responsible only for generating embeddings.
    """

    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

        print("Embedding model loaded.\n")

    def embed_text(self, text):

        return self.model.encode(
            text,
            normalize_embeddings=True
        )

    def embed_chunks(self, chunks):

        vectors = []

        for chunk in chunks:

            embedding = self.embed_text(
                chunk.text
            )

            vectors.append(
                {
                    "chunk": chunk,
                    "embedding": embedding
                }
            )

        return vectors