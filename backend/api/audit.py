from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from jose import jwt

from backend.db import SessionLocal
from backend.auth import SECRET_KEY, ALGORITHM
from backend.services.audit_engine import logger


router = APIRouter(prefix="/audit")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_id(token):

    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload["user_id"]


@router.post("/log")
def log_action(payload: dict):

    logger.log(
        payload["user_id"],
        payload["action"],
        payload["data"]
    )

    return {"status": "logged"}
