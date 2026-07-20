"""
Configuration for ClauseCraft RAG
"""

# Embedding Model
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

VECTOR_DIMENSION = 384

TOP_K = 3

SIMILARITY_THRESHOLD = 0.65

# Gemini Model
LLM_MODEL = "gemini-2.0-flash"