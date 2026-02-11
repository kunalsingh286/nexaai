import streamlit as st
import requests

st.set_page_config(page_title="NexaAI", layout="wide")

st.title("🚀 NexaAI")
st.subheader("AI-Powered Dispute & Collections Platform")

BACKEND_URL = "http://localhost:8000"

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Upload Document", "Extract Fields"]
)

# ---------------- Upload ----------------

if page == "Upload Document":

    st.header("📄 Upload Dispute Document")

    uploaded_file = st.file_uploader(
        "Upload PDF or TXT file",
        type=["pdf", "txt"]
    )

    if uploaded_file and st.button("Process Document"):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type
            )
        }

        res = requests.post(
            f"{BACKEND_URL}/api/ingest",
            files=files
        )

        if res.status_code == 200:

            data = res.json()

            st.session_state["doc_text"] = data["preview"]

            st.success("Document processed!")

            st.text(data["preview"])

        else:
            st.error(res.text)


# ---------------- Extract ----------------

if page == "Extract Fields":

    st.header("🧠 Extract Structured Fields")

    default_text = st.session_state.get("doc_text", "")

    text = st.text_area(
        "Document Text",
        value=default_text,
        height=250
    )

    if st.button("Extract Fields"):

        payload = {"text": text}

        res = requests.post(
            f"{BACKEND_URL}/api/extract",
            json=payload
        )

        if res.status_code == 200:

            data = res.json()

            st.success("Fields extracted!")

            st.json(data["fields"])

        else:
            st.error(res.text)
