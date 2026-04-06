import sys
from annotated_types import doc
from dotenv import load_dotenv
from core.processor import load_and_chunk
from core.vector_store import store_chunks
from core.llm_handler import get_qa_chain

load_dotenv()

def ingest():
    chunks = load_and_chunk("data")
    if chunks:
        store_chunks(chunks)
        print("Ingestion completed successfully.")

def ask(question):
    chain = get_qa_chain()
    result = chain({"query": question})
    
    print("\nAnswer:", result["result"])
    print("\nSource Documents:")
    for doc in result["source_documents"]:
        print(f"- {doc.metadata.get('source_file')} | page {doc.metadata.get('page', '?')}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py ingest")
        print("       python main.py ask 'your question here'")
    elif sys.argv[1] == "ingest":
        ingest()
    elif sys.argv[1] == "ask":
        question = " ".join(sys.argv[2:])
        ask(question)

