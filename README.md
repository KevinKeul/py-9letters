# 🧩 9-Letter Word Puzzle Generator

A Python-based tool designed to automatically generate "Scrambled Word" puzzles from a text file and export them into print-ready PDF documents. 

## Features

*   **Batch Generation:** Automatically pulls words from a local `list.txt` file.
*   **Custom Layouts:** Define exactly how many puzzles appear per page and how they are arranged.
*   **Multi-Page PDFs:** Generate documents with any number of pages in a single run.
*   **Visual Grids:** Creates the classic "9-letter" look found in newspapers and magazines.
*   **Randomized Shuffling:** Each puzzle is automatically scrambled to ensure a challenge.

---

## Getting Started

### Prerequisites
*   **Python 3.x**
*   **ReportLab** as PDF generation library

### Installation

1.  **Clone the repository**
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Use

1.  **Prepare your Wordlist:** 
    Create a file named `list.txt` in the root directory. Add one 9-letter word per line.
2.  **Run the Generator:**
    Launch the script and specify your desired settings (number of puzzles, rows, columns, and total pages):
    ```bash
    python py-9letters.py
    ```
3.  **Output:**
    Your generated PDF will be saved to the project folder as `9letters.pdf`, ready for printing or sharing.

## Input Format (`list.txt`)

Ensure your words are exactly 9 letters long for the best visual result:
```text
ALGORITHM
BLUEPRINT
CHALLENGE
DASHBOARD
...