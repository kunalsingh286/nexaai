from fastapi import APIRouter
from backend.services.draft_engine import engine

router = APIRouter()


@router.post("/")
def generate_draft(payload: dict):
    doc_type = payload.get("type")

    if doc_type == "legal_notice":
        template = "legal_notice.txt"

    elif doc_type == "settlement":
        template = "settlement.txt"

    else:
        return {"error": "Unknown document type"}

    return {
        "document": engine.render(template, payload)
    }
