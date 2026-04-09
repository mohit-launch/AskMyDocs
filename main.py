import sys
import os
from annotated_types import doc
from dotenv import load_dotenv

# Load environment variables FIRST
load_dotenv()
print("API KEY FOUND:", bool(os.getenv("GEMINI_API_KEY")))

# Now use the API key
'''from google import genai
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
print("\nAvailable models:")
for model in client.models.list():
    print(f"  - {model.name}")
'''


from core.processor import load_and_chunk
from core.vector_store import store_chunks
from core.llm_handler import get_qa_chain


def ingest():
    chunks = load_and_chunk("data")
    if chunks:
        store_chunks(chunks)
        print("Ingestion completed successfully.")

def ask(question):
    chain = get_qa_chain()
    result = chain.invoke({"query": question})
    
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