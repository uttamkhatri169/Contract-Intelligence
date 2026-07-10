import unittest

import numpy as np

from rag.vector_store import VectorStore


class VectorStoreFallbackTests(unittest.TestCase):
    def test_search_works_without_faiss(self):
        store = VectorStore()
        store.add_embeddings([
            {"embedding": np.array([1.0, 0.0], dtype="float32"), "chunk": "alpha"},
            {"embedding": np.array([0.0, 1.0], dtype="float32"), "chunk": "beta"},
        ])

        results = store.search(np.array([1.0, 0.0], dtype="float32"), top_k=1)

        self.assertTrue(results)
        self.assertEqual(results[0]["chunk"], "alpha")


if __name__ == "__main__":
    unittest.main()
