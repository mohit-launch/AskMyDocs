import os
import glob
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_chunk(data_dir="data"):
    pdf_files = glob.glob(f"{data_dir}/*.pdf")
    if not pdf_files:
        print("No PDFs found in data/")
        return []

    all_docs = []
    for path in pdf_files:
        loader = PyPDFLoader(path)
        pages = loader.load()
        for page in pages:
            page.metadata["source_file"] = os.path.basename(path)
            page.metadata["total_pages"] = len(pages)
        all_docs.extend(pages)
        print(f"Loaded: {os.path.basename(path)} ({len(pages)} pages)")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", ". ", " ", ""]
    )

    chunks = splitter.split_documents(all_docs)

    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_index"] = i

    print(f"Created {len(chunks)} chunks from {len(all_docs)} pages.")
    return chunks