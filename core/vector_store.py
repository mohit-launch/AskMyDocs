from langchain_community.vectorstores import Chroma
from .embedding import get_embeddings

PERSIST_DIR = "vectorstore"
COLLECTION = "rag_docs"

def store_chunks(chunks):
    db = Chroma.from_documents(
        documents = chunks,
        embeddings = get_embeddings(),
        persistant_dir= PERSIST_DIR,
        collection_name = COLLECTION
    )
    print(f"Stored {len(chunks)} chunks in Chroma vector store.")
    return db

def load_store():
    db =Chroma(
        collection_name = COLLECTION,
        embedding_function = get_embeddings(),
        persistant_dir = PERSIST_DIR
    )
    print("Loaded Chroma vector store.")
    count = db.collection.count()
    if count == 0:
        print("Vector store is empty.")
    print(f"loaded vectorstore ({count} chunks)")
    return db


