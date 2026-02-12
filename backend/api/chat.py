from fastapi import APIRouter, Body, HTTPException

from backend.services.chat_engine import chat_with_user


router = APIRouter()


@router.post("/chat")
def chat(payload: dict = Body(...)):

    try:
        msg = payload.get("message")

        if not msg:
            raise ValueError("Message required")

        reply = chat_with_user(msg)

        return {
            "status": "success",
            "reply": reply
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
