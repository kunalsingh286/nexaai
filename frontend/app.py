import streamlit as st
import requests

st.set_page_config(page_title="NexaAI", layout="wide")

st.title("🚀 NexaAI")
st.subheader("AI-Powered Dispute & Collections Platform")

BACKEND_URL = "http://localhost:8000"

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Upload", "Extract", "Classify", "Legal Assistant"]
)


# ---------------- Upload ----------------

if page == "Upload":

    st.header("📄 Upload Document")

    file = st.file_uploader("Upload PDF/TXT", type=["pdf", "txt"])

    if file and st.button("Process"):

        files = {
            "file": (file.name, file.getvalue(), file.type)
        }

        res = requests.post(
            f"{BACKEND_URL}/api/ingest",
            files=files
        )

        if res.status_code == 200:

            data = res.json()
            st.session_state["doc_text"] = data["preview"]

            st.success("Processed")
            st.text(data["preview"])

        else:
            st.error(res.text)


# ---------------- Extract ----------------

if page == "Extract":

    st.header("🧠 Extract Fields")

    text = st.text_area(
        "Text",
        value=st.session_state.get("doc_text", ""),
        height=250
    )

    if st.button("Extract"):

        res = requests.post(
            f"{BACKEND_URL}/api/extract",
            json={"text": text}
        )

        if res.status_code == 200:

            st.json(res.json()["fields"])

        else:
            st.error(res.text)


# ---------------- Classify ----------------

if page == "Classify":

    st.header("📌 Classify Dispute")

    text = st.text_area(
        "Text",
        value=st.session_state.get("doc_text", ""),
        height=250
    )

    if st.button("Classify"):

        res = requests.post(
            f"{BACKEND_URL}/api/classify",
            json={"text": text}
        )

        if res.status_code == 200:

            data = res.json()["result"]

            st.write("Category:", data["category"])
            st.progress(data["confidence"])

        else:
            st.error(res.text)


# ---------------- Legal RAG ----------------

if page == "Legal Assistant":

    st.header("⚖️ Legal Assistant (RAG)")

    question = st.text_input(
        "Ask legal question"
    )

    if st.button("Ask"):

        res = requests.post(
            f"{BACKEND_URL}/api/rag",
            json={"question": question}
        )

        if res.status_code == 200:

            data = res.json()["data"]

            st.success("Answer")

            st.write("### Answer")
            st.write(data["answer"])

            st.write("### Sources")

            for src in data["sources"]:
                st.code(src)

        else:
            st.error(res.text)
