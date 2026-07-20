# ⚖️ ClauseCraft – AI-Powered Contract Intelligence Platform

> **ClauseCraft** is an end-to-end AI-powered legal document intelligence system that leverages **Retrieval-Augmented Generation (RAG)**, **semantic search**, **vector databases**, and **large language models** to analyze contracts, answer legal questions with citations, extract structured information, identify legal risks, compare agreements, and evaluate retrieval quality.

---

## 📌 Overview

Legal professionals spend a significant amount of time manually reviewing contracts to identify critical clauses such as:

- Termination
- Liability
- Confidentiality
- Non-Compete
- Indemnification
- Governing Law
- Intellectual Property
- Auto Renewal

ClauseCraft automates this process using modern AI techniques.

Instead of manually reading hundreds of pages, users can simply upload a contract and ask questions in natural language.

---

# ✨ Features

## 📄 Multi-format Document Processing

Supports:

- PDF Contracts
- DOCX Contracts

Parses legal documents while preserving:

- Page Numbers
- Paragraphs
- Sections
- Clause Headings

---

## 🧹 Intelligent Document Preprocessing

- Text Cleaning
- Whitespace Normalization
- Paragraph Separation
- Metadata Generation

---

## 🏷 Metadata Generation

Each paragraph is enriched with metadata including:

- Document Name
- Page Number
- Section
- Clause Type
- Paragraph ID

Example:

```json
{
    "document_name": "NDA.pdf",
    "page": 2,
    "section": "Termination",
    "clause_type": "Termination",
    "paragraph_id": 41
}
```

---

# ✂ Clause-Based Chunking

Instead of fixed-size chunks, ClauseCraft performs **legal-aware chunking**.

Chunks are generated based on legal clause boundaries.

Example:

```
Chunk 1

Purpose

----------------

Chunk 2

Confidentiality

----------------

Chunk 3

Termination
```

This significantly improves retrieval quality.

---

# 🧠 Semantic Embeddings

Uses:

- **BAAI/bge-small-en-v1.5**

Advantages:

- Fast
- Lightweight
- High Retrieval Accuracy
- 384-dimensional embeddings

---

# 🗄 Vector Database

Vector Search powered by

- FAISS

Capabilities:

- Index Creation
- Save / Load
- Cosine Similarity Search
- Top-k Retrieval

---

# 🔎 Semantic Retrieval (RAG)

Pipeline

```
Question

↓

Embedding

↓

FAISS Search

↓

Top-k Relevant Clauses

↓

Context Builder

↓

LLM

↓

Answer
```

Example

Question

```
What is the termination clause?
```

Retrieved

```
6. Termination

Either party may terminate this Agreement
by providing thirty (30) days prior written notice...
```

---

# 📚 Citation Engine

Every answer includes evidence.

Example

```
Document:
NDA.pdf

Page:
2

Section:
Termination

Similarity:
0.77
```

This makes the system explainable and auditable.

---

# 🚫 Hallucination Guard

The system avoids hallucinations.

If retrieval confidence falls below a threshold:

```
"I don't know based on the provided contract."
```

instead of generating unsupported answers.

---

# 📄 Structured Extraction

Automatically extracts structured contract information.

Example

```json
{
    "party_a": "...",
    "party_b": "...",
    "effective_date": "...",
    "termination_clause": "...",
    "governing_law": "...",
    "liability_cap": "...",
    "confidentiality_period": "...",
    "non_compete": true
}
```

---

# ⚠ Risk Analysis

Automatically detects legal risks.

Supported Risks

- Unlimited Liability
- Broad Indemnification
- Auto Renewal
- Non Compete
- Confidentiality
- Governing Law
- Termination

Example

```
Termination

LOW

----------------

Non Compete

MEDIUM

----------------

Unlimited Liability

HIGH
```

---

# 📑 Contract Comparison

Compare two contracts side-by-side.

Example

| Clause | Contract A | Contract B | Status |
|---------|------------|------------|--------|
| Termination | 30 Days | 60 Days | Different |
| Governing Law | India | Singapore | Different |
| Confidentiality | 5 Years | 3 Years | Different |

---

# 📊 Evaluation Harness

Measures retrieval quality.

Metrics

- Retrieval Accuracy
- Citation Precision
- Hallucination Rate

Designed for benchmark evaluation using ground-truth question-answer pairs.

---

# 🖥 Streamlit Web Application

Interactive interface providing:

- Upload Contracts
- Ask Questions
- View Citations
- Risk Analysis
- Contract Comparison
- Evaluation Dashboard

---

# 🏗 System Architecture

```
                Upload Contract
                       │
                       ▼
               Document Loader
                       │
                       ▼
               PDF / DOCX Parser
                       │
                       ▼
                Text Preprocessor
                       │
                       ▼
               Metadata Generator
                       │
                       ▼
              Clause-Based Chunker
                       │
                       ▼
                Embedding Generator
                       │
                       ▼
                  FAISS Index
                       │
                       ▼
                Semantic Retriever
                       │
                       ▼
               Context Builder
                       │
                       ▼
              Large Language Model
                       │
                       ▼
      ┌──────────────┼───────────────┐
      ▼              ▼               ▼
 Question Answering  Extraction   Risk Analysis
      │              │               │
      └──────────────┼───────────────┘
                     ▼
               Streamlit Interface
```

---

# 📂 Project Structure

```
ClauseCraft/

app/

comparison/

data/

docs/

evaluation/

ingest/

llm/

parser/

rag/

risk/

Dockerfile

docker-compose.yml

requirements.txt

README.md
```

---

# 🛠 Tech Stack

### Programming

- Python 3.11

### AI

- Sentence Transformers
- BGE Embeddings
- Retrieval-Augmented Generation (RAG)

### Vector Database

- FAISS

### Parsing

- PyMuPDF
- python-docx

### Machine Learning

- NumPy
- Scikit-learn

### Validation

- Pydantic

### UI

- Streamlit

### LLM

- Ollama (Local)
- Provider-based architecture (Gemini/OpenAI extensible)

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ClauseCraft.git

cd ClauseCraft
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
streamlit run app/app.py
```

---

# 📈 Future Improvements

- Hybrid Search (BM25 + Dense Retrieval)
- Cross-Encoder Re-ranking
- OCR Support (Scanned PDFs)
- PostgreSQL + pgvector
- Fine-tuned Legal Models
- Multi-language Contracts
- Agentic Clause Review
- Export Reports (PDF/Excel)

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Large Language Models
- Information Extraction
- Prompt Engineering
- Evaluation of AI Systems
- Python Software Architecture
- Streamlit Application Development
- AI Product Design

---

# 📸 Demo

> Add screenshots or GIFs of:

- Home Page
- Question Answering
- Risk Analysis
- Contract Comparison
- Evaluation Dashboard

---

# 👨‍💻 Author

**Uttam Khatri**

B.Tech Computer Science (AI & ML)

Interested in:

- Artificial Intelligence
- Machine Learning
- NLP
- Generative AI
- Full Stack AI Applications

---

# 📄 License

This project is released under the **MIT License**.

---

⭐ If you found this project useful, consider giving it a star!