import unittest

import ingest.pdf_parser as pdf_parser_module
from ingest.pdf_parser import PDFParser


class FakePage:
    def __init__(self, text):
        self._text = text

    def extract_text(self):
        return self._text


class FakeReader:
    def __init__(self, pages):
        self.pages = pages


class PDFParserFallbackTests(unittest.TestCase):
    def test_extract_text_uses_pypdf_when_fitz_is_unavailable(self):
        original_fitz = pdf_parser_module.fitz
        original_reader = pdf_parser_module.PdfReader

        try:
            pdf_parser_module.fitz = None
            pdf_parser_module.PdfReader = lambda path: FakeReader([
                FakePage("Hello\nworld")
            ])

            parser = PDFParser("dummy.pdf")
            pages = parser.extract_text()

            self.assertEqual(pages[0]["paragraphs"], ["Hello", "world"])
        finally:
            pdf_parser_module.fitz = original_fitz
            pdf_parser_module.PdfReader = original_reader


if __name__ == "__main__":
    unittest.main()
