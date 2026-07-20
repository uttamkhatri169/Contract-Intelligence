from ingest.base_parser import BaseParser
from ingest.utils import save_json


try:
    import fitz  # type: ignore
except BaseException:  # pragma: no cover - exercised when PyMuPDF is unavailable or interrupted
    fitz = None

try:
    from pypdf import PdfReader  # type: ignore
except BaseException:  # pragma: no cover - exercised when pypdf is unavailable or interrupted
    PdfReader = None


class PDFParser(BaseParser):

    def __init__(self, file_path):
        super().__init__(file_path)

    def extract_text(self):
        if fitz is not None:
            document = fitz.open(self.file_path)
            try:
                return self._extract_with_fitz(document)
            finally:
                document.close()

        if PdfReader is not None:
            reader = PdfReader(self.file_path)
            return self._extract_with_pypdf(reader)

        raise ImportError(
            "Unable to read PDF files because neither PyMuPDF nor pypdf is available."
        )

    def _extract_with_fitz(self, document):
        pages = []

        for page_number in range(len(document)):
            page = document.load_page(page_number)
            text = page.get_text()
            paragraphs = [p.strip() for p in text.split("\n") if p.strip()]

            pages.append({
                "document_name": self.document_name,
                "page": page_number + 1,
                "paragraphs": paragraphs
            })

        return pages

    def _extract_with_pypdf(self, reader):
        pages = []

        for page_number, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            paragraphs = [p.strip() for p in text.split("\n") if p.strip()]

            pages.append({
                "document_name": self.document_name,
                "page": page_number + 1,
                "paragraphs": paragraphs
            })

        return pages


if __name__ == "__main__":

    parser = PDFParser("data/contracts/nda/NDA.pdf")

    pages = parser.extract_text()

    save_json(
        pages,
        "data/processed/NDA.json"
    )

    print("PDF Parsed Successfully!")