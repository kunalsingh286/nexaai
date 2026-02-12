from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from jose import jwt

from backend.db import SessionLocal
from backend import models
from backend.auth import SECRET_KEY, ALGORITHM


router = APIRouter(prefix="/cases")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user(token: str, db):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        uid = payload["user_id"]

        user = db.query(models.User)                 .filter(models.User.id == uid)                 .first()

        return user

    except:
        return None


@router.post("/create")
def create_case(
    payload: dict,
    token: str,
    db: Session = Depends(get_db)
):

    user = get_user(token, db)

    if not user:
        raise HTTPException(401, "Invalid token")

    case = models.Case(
        title=payload["title"],
        dispute_type=payload["dispute_type"],
        amount=payload["amount"],
        risk=payload["risk"],
        owner_id=user.id
    )

    db.add(case)
    db.commit()

    return {"status": "case created"}


@router.get("/list")
def list_cases(token: str, db: Session = Depends(get_db)):

    user = get_user(token, db)

    if not user:
        raise HTTPException(401, "Invalid token")

    cases = db.query(models.Case)              .filter(models.Case.owner_id == user.id)              .all()

    return cases
