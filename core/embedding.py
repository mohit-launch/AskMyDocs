from langchain_community.embeddings import HuggingFaceEmbeddings

_embeddings = None 

def get_embeddings():
    global _embeddings 
    if _embeddings is None:
        print("Loading HuggingFaceEmbeddings model...")
        _embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            encode_kwargs={"normalize_embeddings": True}
            )
    return _embeddings
