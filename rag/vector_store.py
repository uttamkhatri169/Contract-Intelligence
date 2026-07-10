import os
import pickle

import numpy as np

from rag.config import VECTOR_DIMENSION

try:
    import faiss  # type: ignore
except Exception:
    faiss = None


class _FallbackIndex:
    """
    Simple in-memory index used when FAISS
    is unavailable.
    """

    def __init__(self, dimension):
        self.dimension = dimension
        self.vectors = []

    def add(self, vectors):
        if vectors.size == 0:
            return

        self.vectors.append(
            np.asarray(vectors, dtype="float32")
        )

    def search(self, query_vector, top_k):

        if not self.vectors:

            return (
                np.empty((1, 0), dtype="float32"),
                np.empty((1, 0), dtype="int64"),
            )

        vectors = np.vstack(self.vectors)

        scores = vectors @ query_vector.T

        scores = scores.reshape(-1)

        top_indices = np.argsort(scores)[::-1][:top_k]

        top_scores = scores[top_indices]

        return (
            top_scores.reshape(1, -1),
            top_indices.reshape(1, -1),
        )


class VectorStore:
    """
    Handles creation, storage,
    loading and searching
    of the vector database.
    """

    def __init__(self):

        if faiss is not None:
            self.index = faiss.IndexFlatIP(
                VECTOR_DIMENSION
            )
        else:
            self.index = _FallbackIndex(
                VECTOR_DIMENSION
            )

        self.metadata = []

    def add_embeddings(self, embedded_chunks):

        vectors = []

        for item in embedded_chunks:

            vectors.append(item["embedding"])

            self.metadata.append(item["chunk"])

        vectors = np.asarray(
            vectors,
            dtype="float32"
        )

        if faiss is not None:
            faiss.normalize_L2(vectors)

        self.index.add(vectors)

        print(
            f"Indexed {len(vectors)} chunks."
        )

    def save(
        self,
        index_path="data/faiss/index.faiss",
        metadata_path="data/faiss/metadata.pkl"
    ):

        os.makedirs(
            os.path.dirname(index_path),
            exist_ok=True
        )

        if faiss is not None:

            faiss.write_index(
                self.index,
                index_path
            )

        else:

            with open(
                index_path,
                "wb"
            ) as file:

                pickle.dump(
                    self.index,
                    file
                )

        with open(
            metadata_path,
            "wb"
        ) as file:

            pickle.dump(
                self.metadata,
                file
            )

        print("Vector database saved.")

    def load(
        self,
        index_path="data/faiss/index.faiss",
        metadata_path="data/faiss/metadata.pkl"
    ):

        if faiss is not None:

            self.index = faiss.read_index(
                index_path
            )

        else:

            with open(
                index_path,
                "rb"
            ) as file:

                self.index = pickle.load(
                    file
                )

        with open(
            metadata_path,
            "rb"
        ) as file:

            self.metadata = pickle.load(
                file
            )

        print("Vector database loaded.")

    def search(
        self,
        query_vector,
        top_k=5
    ):

        if len(self.metadata) == 0:
            return []

        query_vector = np.asarray(
            [query_vector],
            dtype="float32"
        )

        if faiss is not None:
            faiss.normalize_L2(query_vector)

        scores, indices = self.index.search(
            query_vector,
            top_k
        )

        results = []

        for rank, (score, idx) in enumerate(
            zip(scores[0], indices[0]),
            start=1
        ):

            if idx == -1:
                continue

            results.append(
                {
                    "rank": rank,
                    "score": float(score),
                    "chunk": self.metadata[idx],
                }
            )

        return results