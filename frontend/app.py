import streamlit as st
import requests

st.set_page_config(page_title="NexaAI", layout="wide")

st.title("🚀 NexaAI")
st.subheader("AI-Powered Dispute & Collections Platform")

BACKEND_URL = "http://localhost:8000"

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Upload Document"])

if page == "Upload Document":

    st.header("📄 Upload Dispute Document")

    uploaded_file = st.file_uploader(
        "Upload PDF or TXT file",
        type=["pdf", "txt"]
    )

    if uploaded_file and st.button("Process Document"):

        with st.spinner("Processing..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }

            try:
                res = requests.post(
                    f"{BACKEND_URL}/api/ingest",
                    files=files
                )

                if res.status_code == 200:

                    data = res.json()

                    st.success("Document processed!")

                    st.write("### Preview")
                    st.text(data["preview"])

                    st.write("### Metadata")
                    st.json(data)

                else:
                    st.error(res.text)

            except Exception as e:
                st.error(str(e))
