# ClauseCraft – AI-Powered Contract Intelligence

ClauseCraft is an end-to-end Contract Intelligence platform that leverages Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and structured information extraction to automate legal contract analysis.

The system enables users to upload contracts in multiple formats, extract key legal entities, answer natural language questions with clause-level citations, identify potential legal risks, and compare contracts side by side.

---

## Problem Statement

Legal teams spend a significant amount of time manually reviewing contracts to identify:

- Parties involved
- Governing law
- Contract duration
- Termination clauses
- Liability limits
- Indemnification
- Non-compete clauses
- Other legal obligations

ClauseCraft aims to reduce this manual effort by providing an AI-powered assistant capable of understanding legal documents with explainable, citation-backed responses.

---

## Key Features

### Document Ingestion

- PDF support
- DOCX support
- Scanned contract OCR support

### Document Processing

- Text extraction
- Metadata extraction
- Clause-aware chunking
- Semantic chunking

### Retrieval-Augmented Generation (RAG)

- Dense retrieval
- Hybrid search (BM25 + Vector Search)
- Re-ranking
- Inline clause citations
- Confidence scoring
- Hallucination guard

### Structured Extraction

Extract important legal entities including:

- Parties
- Effective Date
- Expiration Date
- Governing Law
- Contract Term
- Termination Clause
- Liability Cap
- Indemnification
- Confidentiality
- Payment Terms

using schema-validated JSON outputs.

### Risk Analysis

Automatically classify clauses into risk categories such as:

- Unlimited Liability
- Broad Indemnity
- Auto Renewal
- Intellectual Property Assignment
- Non-Compete
- Termination Risk
- Jurisdiction Risk
- Confidentiality Risk

### Contract Comparison

Compare two contracts and highlight:

- Added clauses
- Removed clauses
- Modified clauses
- Risk differences

### Evaluation

Evaluate system performance using:

- Exact Match
- Citation Precision
- Hallucination Rate
- Retrieval Accuracy

---

## Proposed Architecture

```
User Upload
      │
      ▼
Document Parsing
      │
      ▼
OCR (if needed)
      │
      ▼
Text Cleaning
      │
      ▼
Clause Chunking
      │
      ▼
Embedding Generation
      │
      ▼
Vector Database
      │
      ▼
Retriever
      │
      ▼
Re-ranker
      │
      ▼
LLM
      │
      ▼
Answer + Citation + Confidence
```

---

## Tech Stack

### Backend

- Python
- FastAPI

### Document Processing

- PyMuPDF
- python-docx
- Tesseract OCR
- Pillow

### Retrieval

- LangChain
- Sentence Transformers
- FAISS / Qdrant
- BM25

### AI

- OpenAI / Gemini
- Hugging Face Transformers
- Pydantic

### Evaluation

- Ragas
- DeepEval

### Frontend

- Streamlit

---

## Project Structure

```
ClauseCraft/
│
├── app/
├── comparison/
├── data/
│   ├── contracts/
│   ├── processed/
│   ├── embeddings/
│   └── evaluation/
├── docs/
├── evaluation/
├── extraction/
├── ingest/
├── parser/
├── rag/
├── risk/
├── tests/
├── notebooks/
├── assets/
│
├── config.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

---

## Development Roadmap

### Week 1

- Repository setup
- Project architecture
- Environment configuration
- Dependency management
- Folder organization
- Dataset preparation
- Documentation

### Week 2

- PDF/DOCX/OCR ingestion
- Clause chunking
- Embedding generation
- Vector database
- Hybrid retrieval
- Citation generation

### Week 3

- Structured extraction
- Risk classification
- Contract comparison

### Week 4

- Evaluation framework
- Streamlit interface
- Deployment
- Documentation
- Final optimization

---

## Current Progress

### Completed

- Repository initialized
- Project architecture designed
- Folder structure organized
- Development environment configured
- Dependency list prepared
- Configuration files added
- Documentation created
- Dataset directory initialized

### In Progress

- Contract collection
- Parser implementation

### Upcoming

- PDF parsing
- OCR pipeline
- RAG pipeline
- Structured extraction
- Risk analysis
- Evaluation framework

---

## Future Improvements

- Fine-tuned legal extraction model
- Multilingual contract support
- Agentic contract review
- Enterprise deployment
- Authentication
- Database persistence

---

## License

This project is developed for educational and portfolio purposes.