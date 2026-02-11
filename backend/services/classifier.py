import joblib
import os


BASE_DIR = os.path.dirname(__file__)

VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")
MODEL_PATH = os.path.join(BASE_DIR, "classifier.pkl")


vectorizer = joblib.load(VECTORIZER_PATH)
model = joblib.load(MODEL_PATH)


def classify_text(text: str):

    X = vectorizer.transform([text])

    probs = model.predict_proba(X)[0]
    classes = model.classes_

    max_idx = probs.argmax()

    return {
        "category": classes[max_idx],
        "confidence": round(float(probs[max_idx]), 3)
    }
