"""
ClauseCraft - Main Entry Point

Pipeline

1. Load Document
2. Parse
3. Preprocess
4. Metadata Generation
5. Chunking
6. Embedding Generation
7. Vector Store
8. Retrieval
9. Context Building
10. Hallucination Guard
11. LLM Answer
12. Citation Engine
13. Structured Extraction
14. Risk Analysis
"""

from ingest.loader import DocumentLoader

from parser.preprocessing import TextPreprocessor
from parser.metadata import MetadataGenerator
from parser.chunker import ClauseChunker
from parser.extraction import ContractExtractor

from rag.embedding_model import EmbeddingModel
from rag.vector_store import VectorStore
from rag.retriever import Retriever
from rag.context_builder import ContextBuilder
from rag.generator import Generator
from rag.citation import CitationEngine
from rag.guardrails import HallucinationGuard

from risk.analyzer import RiskAnalyzer


generator = Generator()
extractor = ContractExtractor()


def build_vector_database(file_path: str):

    print("\n========== DOCUMENT INGESTION ==========\n")

    loader = DocumentLoader(file_path)

    pages = loader.load()

    print(f"Loaded {len(pages)} pages")

    pages = TextPreprocessor.preprocess_document(
        pages
    )

    metadata = MetadataGenerator.generate(
        pages
    )

    print(f"Generated {len(metadata)} metadata records")

    chunks = ClauseChunker.chunk(
        metadata
    )

    print(f"Generated {len(chunks)} chunks")

    embedding_model = EmbeddingModel()

    embedded_chunks = embedding_model.embed_chunks(
        chunks
    )

    vector_store = VectorStore()

    vector_store.add_embeddings(
        embedded_chunks
    )

    vector_store.save()

    print("\nVector Database Ready!\n")


def run_query():

    retriever = Retriever()

    while True:

        query = input(
            "\nAsk a legal question ('exit' to quit): "
        )

        if query.lower() == "exit":
            break

        results = retriever.retrieve(
            query,
            top_k=3
        )

        print("\n========== SEARCH RESULTS ==========\n")

        if len(results) == 0:

            print("No relevant clauses found.")

            continue

        # -----------------------------
        # Retrieved Chunks
        # -----------------------------

        for result in results:

            chunk = result["chunk"]

            print("=" * 70)

            print(f"Rank        : {result['rank']}")

            print(f"Similarity  : {result['score']:.4f}")

            print(f"Document    : {chunk.document_name}")

            print(f"Page        : {chunk.page}")

            print(f"Section     : {chunk.section}")

            print(f"Clause Type : {chunk.clause_type}")

            print()

            print(chunk.text)

            print()

        # -----------------------------
        # Context
        # -----------------------------

        context = ContextBuilder.build(results)

        # -----------------------------
        # Citations
        # -----------------------------

        citations = CitationEngine.generate(results)

        # -----------------------------
        # Hallucination Guard
        # -----------------------------

        if HallucinationGuard.should_answer(results):

            try:

                answer = generator.answer(
                    query,
                    context
                )

            except Exception as e:

                answer = f"LLM generation failed:\n{e}"

        else:

            answer = HallucinationGuard.refusal_message()

        print("\n========== ANSWER ==========\n")

        print(answer)

        # -----------------------------
        # Citations
        # -----------------------------

        CitationEngine.print(citations)

        # -----------------------------
        # Structured Extraction
        # -----------------------------

        print("\n========== STRUCTURED EXTRACTION ==========\n")

        try:

            contract = extractor.extract(
                context
            )

            print(
                contract.model_dump_json(
                    indent=4
                )
            )

        except Exception as e:

            print("Extraction failed.")

            print(e)

        # -----------------------------
        # Risk Analysis
        # -----------------------------

        retrieved_chunks = [

            result["chunk"]

            for result in results

        ]

        risk_report = RiskAnalyzer.analyze(
            retrieved_chunks
        )

        print("\n========== RISK REPORT ==========\n")

        if len(risk_report) == 0:

            print("No significant risks detected.\n")

        else:

            for risk in risk_report:

                print("=" * 70)

                print(f"Clause : {risk.clause}")

                print(f"Risk   : {risk.level}")

                print(f"Reason : {risk.reason}")

                print()

                print(risk.evidence)

                print()


def main():

    file_path = "data/contracts/nda/NDA.pdf"

    build_vector_database(file_path)

    run_query()


if __name__ == "__main__":

    main()
    
    
def compare_demo(contract_a, contract_b):
    
    from comparison.comparator import ContractComparator

    results = ContractComparator.compare(
        contract_a,
        contract_b
    )

    print("\n========== CONTRACT COMPARISON ==========\n")

    for item in results:

        print("=" * 70)

        print(f"Clause : {item.clause}")

        print(f"Contract A : {item.contract_a}")

        print(f"Contract B : {item.contract_b}")

        print(f"Status : {item.status}")

        print()