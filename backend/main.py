from fastapi import FastAPI

from backend.db import engine, Base
from backend import models

from backend.api.ingest import router as ingest_router
from backend.api.extract import router as extract_router
from backend.api.classify import router as classify_router
from backend.api.rag import router as rag_router
from backend.api.chat import router as chat_router
from backend.api.risk import router as risk_router
from backend.api.draft import router as draft_router
from backend.api.users import router as users_router
from backend.api.cases import router as cases_router
from backend.api.explain import router as explain_router
from backend.api.audit import router as audit_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="NexaAI SaaS")


app.include_router(ingest_router)
app.include_router(extract_router)
app.include_router(classify_router)
app.include_router(rag_router)
app.include_router(chat_router)
app.include_router(risk_router)
app.include_router(draft_router)
app.include_router(users_router)
app.include_router(cases_router)
app.include_router(explain_router)
app.include_router(audit_router)


@app.get("/")
def root():
    return {"status": "NexaAI SaaS running"}
