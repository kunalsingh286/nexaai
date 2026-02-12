from fastapi import APIRouter
from backend.services.risk_engine import RiskEngine

router = APIRouter()

engine = RiskEngine()


@router.post("/risk/predict")
def predict_risk(payload: dict):
    return engine.predict(payload)
