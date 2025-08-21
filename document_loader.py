
import os
from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document

def load_text_file(filepath):
	"""Load and return the contents of a plain text file."""
	with open(filepath, 'r', encoding='utf-8') as f:
		return f.read()

def load_pdf_file(filepath):
	"""Extract and return text from a PDF file."""
	return extract_pdf_text(filepath)

def load_word_file(filepath):
	"""Extract and return text from a Word (.docx) file."""
	doc = Document(filepath)
	return '\n'.join([para.text for para in doc.paragraphs])

def load_document(filepath):
	"""Detect file type and load document accordingly."""
	ext = os.path.splitext(filepath)[1].lower()
	if ext == '.txt':
		return load_text_file(filepath)
	elif ext == '.pdf':
		return load_pdf_file(filepath)
	elif ext == '.docx':
		return load_word_file(filepath)
	else:
		raise ValueError(f"Unsupported file type: {ext}")
