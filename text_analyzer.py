"""Text Analyzer - Final Refactor with Comments

This script refactors the provided starter into a clean, modular, and Pythonic program.

Features:
- PEP 8 names and docstrings
- Context manager for file I/O
- collections.Counter for frequencies
- List comprehension for long words
- Modular functions
- CLI with argparse
"""

from collections import Counter
from pathlib import Path
import argparse

def read_text(path: Path) -> str:
    """Safely read text from a file using a context manager."""
    with path.open("r", encoding="utf-8") as f:
        return f.read()

def tokenize_words(text: str):
    """Convert text to lowercase and split on whitespace."""
    return text.lower().split()

def count_words(words):
    """Return a Counter object of word frequencies."""
    return Counter(words)

def find_long_words(words, min_length=4):
    """Return a list of words with length >= min_length."""
    return [w for w in words if len(w) >= min_length]

def top_n_words(freqs, n=5):
    """Return the top n most frequent words as (word, count)."""
    return freqs.most_common(n)

def analyze_text(path: Path, *, top=5, min_length=4):
    """Perform the full analysis and print results."""
    text = read_text(path)
    words = tokenize_words(text)
    freqs = count_words(words)
    long_words = find_long_words(words, min_length)

    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(freqs)}")
    print("Top words:")
    for word, count in top_n_words(freqs, top):
        print(f"  '{word}': {count}")
    print(f"Long words (length ≥ {min_length}): {len(long_words)}")

def parse_args():
    """Parse CLI arguments for file path and analysis options."""
    parser = argparse.ArgumentParser(description="Analyze a text file.")
    parser.add_argument("path", nargs="?", default="sample.txt",
                        help="Path to the text file (default: sample.txt)")
    parser.add_argument("--top", type=int, default=5,
                        help="Top-N most frequent words (default: 5)")
    parser.add_argument("--min-length", type=int, default=4,
                        help="Minimum length for a word to count as 'long'")
    return parser.parse_args()

def main():
    """Entry point for command line execution."""
    args = parse_args()
    analyze_text(Path(args.path), top=args.top, min_length=args.min_length)

if __name__ == "__main__":
    main()
