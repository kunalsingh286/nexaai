from fastapi import FastAPI
from backend.db.models import Base
from backend.db.session import engine

from backend.api.users import router as users_router
from backend.api.chat import router as chat_router
from backend.api.classify import router as classify_router
from backend.api.risk import router as risk_router
from backend.api.ingest import router as ingest_router
from backend.api.rag import router as rag_router
from backend.api.draft import router as draft_router
from backend.api.explain import router as explain_router
from backend.api.audit import router as audit_router

app = FastAPI(title="NexaAI SaaS")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "NexaAI SaaS running"}

@app.get("/health")
def health():
    return {"status": "healthy"}


# Register APIs
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(chat_router, tags=["Chat"])
app.include_router(classify_router, tags=["Classify"])
app.include_router(risk_router, tags=["Risk"])
app.include_router(ingest_router, prefix="/ingest", tags=["Ingest"])
app.include_router(rag_router, prefix="/rag", tags=["RAG"])
app.include_router(draft_router, prefix="/draft", tags=["Draft"])
app.include_router(explain_router, prefix="/explain", tags=["Explain"])
app.include_router(audit_router, tags=["Audit"])
