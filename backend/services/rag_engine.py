from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

import os


INDEX_DIR = "data/faiss_index"


def load_rag_chain():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        INDEX_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = db.as_retriever(search_kwargs={"k": 3})

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return chain


rag_chain = load_rag_chain()


def ask_legal_question(question: str):

    result = rag_chain({"query": question})

    answer = result["result"]

    sources = []

    for doc in result["source_documents"]:
        sources.append(doc.page_content[:200])

    return {
        "answer": answer,
        "sources": sources
    }
