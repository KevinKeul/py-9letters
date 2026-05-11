# 🧩 9-Letter Word Puzzle Generator

A Python-based tool designed to automatically generate "Scrambled Word" puzzles from a text file and export them into print-ready PDF documents. 

![Example with the german word \"Hauskatze\"](example.png "Example with the german word \"Hauskatze\"")

Example with the german word \"Hauskatze\"

## Features

* **Batch Generation:** Automatically pulls words from a local word list file.
* **Centralized Configuration:** Manage all settings (colors, files, layouts) via a single `config.toml` file.
* **Custom Layouts:** Define exactly how many puzzles appear per page and how they are arranged.
* **Custom Styling:** Easily change fonts, text colors, and the "special" square highlight color.
* **Multi-Page PDFs:** Generate documents with any number of pages in a single run.
* **Visual Grids:** Creates the classic "9-letter" look found in newspapers and magazines.
* **Randomized Shuffling:** Each puzzle is automatically scrambled to ensure a challenge.

## Getting Started

### Prerequisites
* **Python 3.x**
* **tomllib** for configuration file (built-in library)
* **ReportLab** as PDF generation library

### Installation

1. **Clone the repository**
2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Use

1. **Prepare your Wordlist:** 
    Create a file for word list (default `list.txt`) in the root directory. Add one 9-letter word per line.
2. **Adjust settings:** 
    Open `config.toml` to set your desired file paths, page number, colors, page margins, and grid size.
3. **Run the Generator:**
    Launch the script with the specified settings:
    ```bash
    python py-9letters.py
    ```
4. **Output:**
    Your generated PDF will be saved, ready for printing or sharing.

## Input Format Example

Ensure your words are exactly 9 letters long for the best visual result:
```text
ALGORITHM
BLUEPRINT
CHALLENGE
DASHBOARD
...
````


## Configuration (`config.toml`)

Before running the script, customize your output in the `config.toml` file:
```toml
[files]
input_word_list = "list.txt"
output_pdf = "9letters.pdf"

[page]
total_pages = 3
grid_columns = 1
grid_rows = 2
margin_inches = 1.0

[style]
font_name = "Helvetica-Bold"
text_color = "black"
special_bg_color = "red"
special_text_color = "white"
```

