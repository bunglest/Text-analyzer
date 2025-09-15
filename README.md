# Pythonic Text Analyzer

## Overview
This project refactors a provided unpythonic script (`unpythonic_analyzer.py`) into a clean, modular, and Pythonic program (`text_analyzer.py`).  
The analyzer reads a text file and reports:
- Total number of words  
- Number of unique words  
- The top **N** most frequent words  
- The number of "long" words (greater than a given length, default 3)  

## How to Run
Make sure you have Python 3 installed. From the repository root:

```bash
# Default run (analyzes sample.txt, shows top 5 words, long words >= 4 chars)
python text_analyzer.py

# Analyze a different file
python text_analyzer.py myfile.txt

# Customize top-N and min-length
python text_analyzer.py sample.txt --top 10 --min-length 6


By default, if no file path is provided, the program will attempt to analyze sample.txt.

Refactoring Highlights

The starter code (unpythonic_analyzer.py) was intentionally full of bad practices.
The refactored solution (text_analyzer.py) addresses these issues by:

✅ PEP 8 Compliance

Snake_case naming for all variables and functions

Proper indentation and spacing

Descriptive docstrings and inline comments

✅ Idiomatic Python Features

Context manager (with open(...)) for safe file handling

List comprehension to build the long_words list

collections.Counter to efficiently count word frequencies

✅ Improved Structure & Modularity

Functions split into small, reusable helpers (read_text, tokenize_words, count_words, find_long_words, top_n_words)

analyze_text orchestrates the workflow

if __name__ == "__main__": guard with a main() function for clean CLI use

✅ Readable Output

All print statements use f-strings

Results are clearly formatted for the user

Repository Contents

unpythonic_analyzer.py – the original starter file (unrefactored)

text_analyzer.py – the refactored and Pythonic solution

sample.txt – a simple test file

README.md – this documentation

Screencast

You will need to record a 3–5 minute video walkthrough for submission. Include the link here:

🎥 Screencast Link: [PLACEHOLDER – paste Loom or YouTube link here]

Checklist for the screencast:

Run the program from the terminal to demonstrate correct functionality.

Show the use of the context manager in the code.

Point out the list comprehension for long words.

Explain the benefits of Counter over a manual dictionary loop.

Highlight how the code follows PEP 8 and is broken into modular functions.