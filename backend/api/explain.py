from fastapi import APIRouter
from backend.services.explain_engine import engine


router = APIRouter(prefix="/explain")


@router.post("/risk")
def explain_risk(payload: dict):

    explanation = engine.explain_risk(payload)

    return {
        "explanation": explanation
    }
