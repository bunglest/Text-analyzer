# Pythonic Text Analyzer

## Overview
The purpose of this project is to take an unpythonic, poorly written script (`unpythonic_analyzer.py`) and refactor it into a clean, efficient, and Pythonic program (`text_analyzer.py`).  
The analyzer processes a text file and reports:
- Total number of words  
- Number of unique words  
- The top **N** most frequent words  
- The number of "long" words (greater than a given length, default 3)  

This demonstrates applying best practices, including PEP 8, idiomatic Python features, and modular design.

## How to Run
Make sure you have Python 3 installed. From the repository root, run:

```bash
# Default run (analyzes sample.txt, shows top 5 words, long words >= 4 chars)
python text_analyzer.py

# Analyze a different file
python text_analyzer.py myfile.txt

# Customize top-N and min-length
python text_analyzer.py sample.txt --top 10 --min-length 6


By default, if no file path is provided, the program will attempt to analyze sample.txt.

Key Improvements in Refactoring

The starter code (unpythonic_analyzer.py) was intentionally full of bad practices.
The refactored version (text_analyzer.py) introduces the following improvements:

PEP 8 Compliance

Renamed variables and functions to snake_case.

Added clear docstrings and comments.

Proper spacing and indentation applied consistently.

Context Manager for File Handling

Replaced manual open() and close() calls with a with open(...) block to ensure safe and automatic file closure.

List Comprehension

Replaced the inefficient loop that appended to long_words with a concise one-line list comprehension.

collections.Counter

Used Counter to simplify and speed up word frequency counting, replacing the verbose manual dictionary loop.

Modularity & Reusability

Split the code into small helper functions (read_text, tokenize_words, count_words, find_long_words, top_n_words).

Added a main() function and if __name__ == "__main__": guard for reuse and clean structure.

These changes improve readability, efficiency, and maintainability while preserving the original script’s functionality.