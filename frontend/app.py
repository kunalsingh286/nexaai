import streamlit as st
import requests

st.set_page_config(page_title="NexaAI", layout="wide")

st.title("🚀 NexaAI")
st.subheader("AI-Powered Dispute & Collections Platform")

BACKEND_URL = "http://localhost:8000"

st.info("Phase 0: System Initialized")

if st.button("Check Backend Health"):
    try:
        res = requests.get(BACKEND_URL)
        st.success(res.json())
    except Exception as e:
        st.error(f"Backend not reachable: {e}")
