import os
import faiss
import numpy as np
import pickle

from sentence_transformers import SentenceTransformer
import ollama


INDEX_PATH = "data/faiss_index/index.faiss"
META_PATH = "data/faiss_index/meta.pkl"


model = SentenceTransformer("all-MiniLM-L6-v2")


def load_index():

    index = faiss.read_index(INDEX_PATH)

    with open(META_PATH, "rb") as f:
        texts = pickle.load(f)

    return index, texts


index, texts = load_index()


def search_docs(query, k=3):

    emb = model.encode([query])
    D, I = index.search(np.array(emb).astype("float32"), k)

    results = []

    for idx in I[0]:
        if idx < len(texts):
            results.append(texts[idx])

    return results


def ask_legal_question(question: str):

    docs = search_docs(question)

    context = "\n\n".join(docs)

    prompt = f"""
You are a legal assistant for Indian business disputes.

Context:
{context}

Question:
{question}

Answer clearly with legal basis.
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    answer = response["message"]["content"]

    return {
        "answer": answer,
        "sources": docs
    }
