from fastapi import APIRouter, Body, HTTPException

from backend.services.extractor import extract_fields

router = APIRouter()


@router.post("/extract")
def extract_from_text(payload: dict = Body(...)):

    try:
        text = payload.get("text")

        if not text:
            raise ValueError("Text is required")

        fields = extract_fields(text)

        return {
            "status": "success",
            "fields": fields
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
