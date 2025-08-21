import subprocess
import time
import requests
# Entry point for the chatbot CLI



import os
import getpass
from document_loader import load_document, chunk_text, build_vector_store, retrieve_relevant_chunks, generate_answer
from config import DATA_DIR

def summarize_matches(matches):
    """Return a summary of matched text snippets."""
    # Deprecated: now using LLM-based answer generation
    return "No relevant information found."

def search_documents(question, data_dir):
    """Search all documents for relevant information related to the question."""
    # Deprecated: now using vector store and LLM
    return {}

def main():
    # Check if Ollama is running
    def is_ollama_running(url="http://localhost:11434/api/generate"):
        try:
            response = requests.post(url, json={"model": "llama3", "prompt": "ping", "stream": False}, timeout=2)
            return response.status_code == 200
        except Exception:
            return False

    if not is_ollama_running():
        print("Ollama is not running. Attempting to start Ollama with model 'llama3'...")
        try:
            subprocess.Popen(["ollama", "run", "llama3"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            # Wait for Ollama to start
            for _ in range(20):
                if is_ollama_running():
                    print("Ollama started successfully.")
                    break
                time.sleep(1)
            else:
                print("Warning: Ollama did not start. Please start it manually.")
        except Exception as e:
            print(f"Error starting Ollama: {e}")
    print("Welcome to the Document Chatbot!")
    print("Type your question, or 'exit' to quit.")
    # Load and chunk all documents
    all_chunks = []
    print("\nLoading and chunking documents...")
    for fname in os.listdir(DATA_DIR):
        fpath = os.path.join(DATA_DIR, fname)
        if not os.path.isfile(fpath):
            continue
        try:
            text = load_document(fpath)
            chunks = chunk_text(text)
            all_chunks.extend(chunks)
        except Exception as e:
            print(f"Warning: Could not process {fname}: {e}")

    # Build vector store
    print("Building vector store...")
    vector_store = build_vector_store(all_chunks)

    while True:
        question = input("\nYour question: ").strip()
        if question.lower() in ("exit", "quit"):
            print("Goodbye!")
            break
        print("\nRetrieving relevant information...")
        relevant_chunks = retrieve_relevant_chunks(vector_store, question, k=5)
        print("\nGenerating answer...")
        answer = generate_answer(question, relevant_chunks)
        print("\nAnswer:")
        print(answer)

if __name__ == "__main__":
    main()
