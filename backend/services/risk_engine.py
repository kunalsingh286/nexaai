import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier, XGBRegressor
from sklearn.ensemble import RandomForestClassifier


DATA_PATH = "data/risk_training.csv"
MODEL_PATH = "models/"


class RiskEngine:

    def __init__(self):
        self.encoder = LabelEncoder()

    def train(self):

        df = pd.read_csv(DATA_PATH)

        df["dispute_type"] = self.encoder.fit_transform(df["dispute_type"])

        X = df[[
            "dispute_type",
            "amount",
            "delay_days",
            "doc_length",
            "sentiment",
            "legal_strength"
        ]]

        y_win = df["win"]
        y_settle = df["settled"]
        y_days = df["days_to_resolve"]

        X_train, X_test, y_win_train, _ = train_test_split(
            X, y_win, test_size=0.2, random_state=42
        )

        # Win Predictor
        win_model = XGBClassifier(
            n_estimators=100,
            max_depth=4,
            learning_rate=0.1,
            eval_metric="logloss"
        )
        win_model.fit(X_train, y_win_train)

        # Settlement Predictor
        settle_model = RandomForestClassifier(
            n_estimators=100,
            max_depth=6
        )
        settle_model.fit(X, y_settle)

        # Time Predictor
        time_model = XGBRegressor(
            n_estimators=120,
            max_depth=4,
            learning_rate=0.1
        )
        time_model.fit(X, y_days)

        joblib.dump(win_model, MODEL_PATH + "win.pkl")
        joblib.dump(settle_model, MODEL_PATH + "settle.pkl")
        joblib.dump(time_model, MODEL_PATH + "time.pkl")
        joblib.dump(self.encoder, MODEL_PATH + "encoder.pkl")

        print("Risk models trained successfully.")


    def predict(self, data: dict):

        win_model = joblib.load(MODEL_PATH + "win.pkl")
        settle_model = joblib.load(MODEL_PATH + "settle.pkl")
        time_model = joblib.load(MODEL_PATH + "time.pkl")
        encoder = joblib.load(MODEL_PATH + "encoder.pkl")

        dispute = encoder.transform([data["dispute_type"]])[0]

        X = [[
            dispute,
            data["amount"],
            data["delay_days"],
            data["doc_length"],
            data["sentiment"],
            data["legal_strength"]
        ]]

        win_prob = win_model.predict_proba(X)[0][1]
        settle_prob = settle_model.predict_proba(X)[0][1]
        days = int(time_model.predict(X)[0])

        risk = "Low"
        if win_prob < 0.4:
            risk = "High"
        elif win_prob < 0.7:
            risk = "Medium"

        return {
            "win_probability": round(float(win_prob), 2),
            "settlement_chance": round(float(settle_prob), 2),
            "expected_days": days,
            "risk": risk
        }
