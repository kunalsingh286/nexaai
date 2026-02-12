from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.db import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    cases = relationship("Case", back_populates="owner")


class Case(Base):

    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)
    dispute_type = Column(String)
    amount = Column(Float)
    risk = Column(String)

    owner_id = Column(Integer, ForeignKey("users.id"))

    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="cases")
