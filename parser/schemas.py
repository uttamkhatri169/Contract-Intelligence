from pydantic import BaseModel
from typing import List


class Paragraph(BaseModel):

    paragraph_id: int

    document_name: str

    page: int

    section: str

    clause_type: str

    text: str


class Chunk(BaseModel):

    chunk_id: int

    document_name: str

    page: int

    section: str

    clause_type: str

    paragraph_ids: List[int]

    text: str

    character_count: int

    word_count: int

    estimated_tokens: int