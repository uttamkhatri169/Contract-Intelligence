from parser.schemas import Chunk 
class ClauseChunker:
    """
    Groups consecutive paragraphs belonging
    to the same legal section.
    """

    @staticmethod
    def chunk(metadata):

        chunks = []

        current_chunk = None

        chunk_id = 1

        for item in metadata:

            # First chunk
            if current_chunk is None:

               current_chunk = Chunk(
                    chunk_id=chunk_id,
                    document_name=item["document_name"],
                    page=item["page"],
                    section=item["section"],
                    clause_type=item["clause_type"],
                    paragraph_ids=[item["paragraph_id"]],
                    text=item["text"],
                    character_count=len(item["text"]),
                    word_count=len(item["text"].split()),
                    estimated_tokens=int(len(item["text"].split()) * 1.3)
                )

            else:

                # Same section
                if item["section"] == current_chunk.section:

                    current_chunk.text += "\n" + item["text"]

                    current_chunk.paragraph_ids.append(
                        item["paragraph_id"]
                    )

                    current_chunk.character_count = len(current_chunk.text)

                    current_chunk.word_count = len(
                        current_chunk.text.split()
                    )

                    current_chunk.estimated_tokens = int(
                        current_chunk.word_count * 1.3
                    )

                # New section
                else:

                    chunks.append(current_chunk)

                    chunk_id += 1

                    current_chunk = Chunk(
                        chunk_id=chunk_id,
                        document_name=item["document_name"],
                        page=item["page"],
                        section=item["section"],
                        clause_type=item["clause_type"],
                        paragraph_ids=[item["paragraph_id"]],
                        text=item["text"],
                        character_count=len(item["text"]),
                        word_count=len(item["text"].split()),
                        estimated_tokens=int(len(item["text"].split()) * 1.3)
                    )

        if current_chunk is not None:
            chunks.append(current_chunk)

        return chunks