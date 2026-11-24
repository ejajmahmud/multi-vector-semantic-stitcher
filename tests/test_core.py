"""Tests for SemanticStitcher."""
import unittest
from multi_vector_semantic_stitcher.core import SemanticStitcher, ChunkSpan

class TestSemanticStitcher(unittest.TestCase):
    def test_clean_stitching(self):
        c1 = ChunkSpan("d1", 0, "The quick brown fox jumps over the")
        c2 = ChunkSpan("d1", 1, "fox jumps over the lazy dog.")

        stitched = SemanticStitcher.stitch([c1, c2])
        self.assertEqual(stitched, "The quick brown fox jumps over the lazy dog.")
