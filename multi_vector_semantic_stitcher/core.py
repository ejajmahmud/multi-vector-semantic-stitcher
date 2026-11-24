"""Core Semantic Stitcher implementation."""
from typing import List

class ChunkSpan:
    def __init__(self, doc_id: str, chunk_index: int, text: str):
        self.doc_id = doc_id
        self.chunk_index = chunk_index
        self.text = text

class SemanticStitcher:
    @staticmethod
    def _find_overlap(tail: str, head: str, min_overlap: int = 10) -> int:
        max_check = min(len(tail), len(head))
        for l in range(max_check, min_overlap - 1, -1):
            if tail.endswith(head[:l]):
                return l
        return 0

    @classmethod
    def stitch(cls, chunks: List[ChunkSpan]) -> str:
        if not chunks:
            return ""
        sorted_chunks = sorted(chunks, key=lambda c: c.chunk_index)
        stitched = sorted_chunks[0].text

        for c in sorted_chunks[1:]:
            overlap_len = cls._find_overlap(stitched, c.text)
            if overlap_len > 0:
                stitched += c.text[overlap_len:]
            else:
                stitched += " " + c.text

        return stitched
