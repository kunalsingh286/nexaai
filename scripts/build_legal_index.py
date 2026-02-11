import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


DATA_DIR = "data/corpora"
INDEX_DIR = "data/faiss_index"


def load_documents():
    docs = []

    for fname in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, fname)

        with open(path, "r", encoding="utf-8") as f:
            docs.append(f.read())

    return docs


def main():

    docs = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = []

    for doc in docs:
        chunks.extend(splitter.split_text(doc))

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_texts(chunks, embeddings)

    os.makedirs(INDEX_DIR, exist_ok=True)
    db.save_local(INDEX_DIR)

    print("Legal index built successfully.")


if __name__ == "__main__":
    main()
