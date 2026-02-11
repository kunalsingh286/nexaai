import streamlit as st
import requests

st.set_page_config(page_title="NexaAI", layout="wide")

st.title("🚀 NexaAI")
st.subheader("AI-Powered Dispute & Collections Platform")

BACKEND_URL = "http://localhost:8000"

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Upload Document", "Extract Fields", "Classify Dispute"]
)

# ---------------- Upload ----------------

if page == "Upload Document":

    st.header("📄 Upload Document")

    uploaded_file = st.file_uploader(
        "Upload PDF or TXT",
        type=["pdf", "txt"]
    )

    if uploaded_file and st.button("Process"):

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

            st.success("Processed")

            st.text(data["preview"])

        else:
            st.error(res.text)


# ---------------- Extract ----------------

if page == "Extract Fields":

    st.header("🧠 Extract Fields")

    default_text = st.session_state.get("doc_text", "")

    text = st.text_area(
        "Text",
        value=default_text,
        height=250
    )

    if st.button("Extract"):

        res = requests.post(
            f"{BACKEND_URL}/api/extract",
            json={"text": text}
        )

        if res.status_code == 200:

            st.success("Extracted")
            st.json(res.json()["fields"])

        else:
            st.error(res.text)


# ---------------- Classify ----------------

if page == "Classify Dispute":

    st.header("📌 Dispute Classification")

    default_text = st.session_state.get("doc_text", "")

    text = st.text_area(
        "Text for Classification",
        value=default_text,
        height=250
    )

    if st.button("Classify"):

        res = requests.post(
            f"{BACKEND_URL}/api/classify",
            json={"text": text}
        )

        if res.status_code == 200:

            data = res.json()["result"]

            st.success("Classification Complete")

            st.write("### Category")
            st.write(data["category"])

            st.write("### Confidence")
            st.progress(data["confidence"])

        else:
            st.error(res.text)
