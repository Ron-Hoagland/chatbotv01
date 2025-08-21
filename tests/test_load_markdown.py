import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from document_loader import load_markdown_file
from config import DATA_DIR

def test_load_markdown():
    md_path = os.path.join(DATA_DIR, "sample.md")
    try:
        text = load_markdown_file(md_path)
        print("Markdown file loaded successfully. First 500 characters:")
        print(text[:500])
    except Exception as e:
        print(f"Error loading Markdown file: {e}")

if __name__ == "__main__":
    test_load_markdown()
