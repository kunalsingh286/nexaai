from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.logger import setup_logger

from backend.api.ingest import router as ingest_router
from backend.api.extract import router as extract_router
from backend.api.classify import router as classify_router
from backend.api.rag import router as rag_router
from backend.api.chat import router as chat_router


logger = setup_logger()

app = FastAPI(
    title="NexaAI API",
    description="AI-powered Dispute & Collections Platform",
    version="0.5.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingest_router, prefix="/api")
app.include_router(extract_router, prefix="/api")
app.include_router(classify_router, prefix="/api")
app.include_router(rag_router, prefix="/api")
app.include_router(chat_router, prefix="/api")


@app.get("/")
def health_check():
    logger.info("health_check_called")
    return {"status": "NexaAI backend running"}
