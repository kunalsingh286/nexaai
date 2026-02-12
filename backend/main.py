from fastapi import FastAPI

from backend.api.ingest import router as ingest_router
from backend.api.extract import router as extract_router
from backend.api.classify import router as classify_router
from backend.api.rag import router as rag_router
from backend.api.chat import router as chat_router
from backend.api.risk import router as risk_router


app = FastAPI(title="NexaAI")


app.include_router(ingest_router)
app.include_router(extract_router)
app.include_router(classify_router)
app.include_router(rag_router)
app.include_router(chat_router)
app.include_router(risk_router)


@app.get("/")
def root():
    return {"status": "NexaAI running"}
