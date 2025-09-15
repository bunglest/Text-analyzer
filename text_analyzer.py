from collections import Counter
from pathlib import Path

def read_text(path: Path) -> str:
    """Read and return full file contents (UTF-8)."""
    with path.open("r", encoding="utf-8") as f:
        return f.read()

def tokenize_words(text: str):
    """Return lowercase words split on whitespace."""
    return text.lower().split()

def count_words(words):
    """Count word frequencies using Counter."""
    return Counter(words)

def find_long_words(words, min_length=4):
    """Return words of length >= min_length."""
    return [w for w in words if len(w) >= min_length]

def top_n_words(freqs, n=5):
    """Return top n most frequent words."""
    return freqs.most_common(n)

def analyze_text(path: Path, *, top=5, min_length=4):
    """Run full text analysis and print results."""
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

if __name__ == "__main__":
    analyze_text(Path("sample.txt"))