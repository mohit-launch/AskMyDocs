from langchain_community.vectorstores import Chroma
from .embedding import get_embeddings

PERSIST_DIR = "vectorstore"
COLLECTION = "rag_docs"

def store_chunks(chunks):
    db = Chroma.from_documents(
        documents = chunks,
        embedding = get_embeddings(),
        persist_directory= PERSIST_DIR,
        collection_name = COLLECTION
    )
    print(f"Stored {len(chunks)} chunks in Chroma vector store.")
    return db

def load_store():
    db =Chroma(
        collection_name = COLLECTION,
        embedding_function = get_embeddings(),
        persist_directory = PERSIST_DIR
    )
    print("Loaded Chroma vector store.")
    count = db._collection.count()
    if count == 0:
        print("Vector store is empty.")
    print(f"loaded vectorstore ({count} chunks)")
    return db


