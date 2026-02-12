from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.db import SessionLocal
from backend import models
from backend.auth import hash_password, verify_password, create_token


router = APIRouter(prefix="/users")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/signup")
def signup(data: dict, db: Session = Depends(get_db)):

    user = db.query(models.User)             .filter(models.User.email == data["email"])             .first()

    if user:
        raise HTTPException(400, "User exists")

    new_user = models.User(
        email=data["email"],
        hashed_password=hash_password(data["password"])
    )

    db.add(new_user)
    db.commit()

    return {"status": "created"}


@router.post("/login")
def login(data: dict, db: Session = Depends(get_db)):

    user = db.query(models.User)             .filter(models.User.email == data["email"])             .first()

    if not user:
        raise HTTPException(400, "Invalid login")

    if not verify_password(data["password"], user.hashed_password):
        raise HTTPException(400, "Invalid login")

    token = create_token({"user_id": user.id})

    return {"access_token": token}
