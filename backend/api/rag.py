from fastapi import APIRouter, Body, HTTPException

from backend.services.rag_engine import ask_legal_question


router = APIRouter()


@router.post("/ask")
def legal_rag(payload: dict = Body(...)):

    try:
        question = payload.get("question")

        if not question:
            raise ValueError("Question required")

        result = ask_legal_question(question)

        return {
            "status": "success",
            "data": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
