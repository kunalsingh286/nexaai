from fastapi import APIRouter, Body, HTTPException

from backend.services.classifier import classify_text

router = APIRouter()


@router.post("/classify")
def classify(payload: dict = Body(...)):

    try:
        text = payload.get("text")

        if not text:
            raise ValueError("Text is required")

        result = classify_text(text)

        return {
            "status": "success",
            "result": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
