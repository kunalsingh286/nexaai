import os
import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer


DATA_DIR = "data/corpora"
OUT_DIR = "data/faiss_index"

model = SentenceTransformer("all-MiniLM-L6-v2")


def load_docs():

    docs = []

    for f in os.listdir(DATA_DIR):

        path = os.path.join(DATA_DIR, f)

        with open(path, "r", encoding="utf-8") as file:
            docs.append(file.read())

    return docs


def main():

    texts = load_docs()

    embeddings = model.encode(texts)

    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)

    index.add(np.array(embeddings).astype("float32"))

    os.makedirs(OUT_DIR, exist_ok=True)

    faiss.write_index(index, f"{OUT_DIR}/index.faiss")

    with open(f"{OUT_DIR}/meta.pkl", "wb") as f:
        pickle.dump(texts, f)

    print("FAISS index rebuilt.")


if __name__ == "__main__":
    main()
