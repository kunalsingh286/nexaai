from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.logger import setup_logger

logger = setup_logger()

app = FastAPI(
    title="NexaAI API",
    description="AI-powered Dispute & Collections Platform",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    logger.info("health_check_called")
    return {"status": "NexaAI backend running"}
