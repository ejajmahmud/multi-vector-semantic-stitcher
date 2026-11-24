"""CLI for Semantic Stitcher."""
import argparse
from .core import SemanticStitcher, ChunkSpan

def main():
    parser = argparse.ArgumentParser(description="Multi-Vector Semantic Stitcher CLI")
    parser.add_argument("--demo", action="store_true", help="Run chunk stitching demo")
    args = parser.parse_args()

    c1 = ChunkSpan("doc1", 0, "def calculate_tax(amount): return amount * ")
    c2 = ChunkSpan("doc1", 1, "return amount * 0.15 # finished")

    result = SemanticStitcher.stitch([c1, c2])
    print("Stitched Continuous Code Block:")
    print(" ", result)

if __name__ == "__main__":
    main()
