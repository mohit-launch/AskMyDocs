import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from .vector_store import load_store

PROMPT_TEMPLATE ="""
You are a helpful assistant. Use ONLY the context below to answer.
If the answer is not present, say "I don't know based on the provided documents."

Context:
{context}

Question: {question}
Answer : """

def get_qa_chain():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    prompt = PromptTemplate(
        template = PROMPT_TEMPLATE,
        input_variables = ["context", "question"]
    )
    
    retriever = load_store().as_retriever(search_kwargs={"k": 5})
    chain = RetrievalQA.from_chain_type(
        llm = llm,
        retriever = retriever,
        chain_type_kwargs = {"prompt": prompt},
        return_source_documents = True
    )
    return chain