import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# Synthetic training data
texts = [
    "payment is delayed and invoice is unpaid",
    "late payment pending for 60 days",
    "amount not received on due date",

    "goods are defective and quality is poor",
    "fabric quality not acceptable",
    "product has defects",

    "less quantity delivered than agreed",
    "short supply of goods",
    "missing items in shipment",

    "contract breached and terms violated",
    "delivery not as per contract",
    "agreement was violated"
]

labels = [
    "Delayed Payment",
    "Delayed Payment",
    "Delayed Payment",

    "Quality Dispute",
    "Quality Dispute",
    "Quality Dispute",

    "Quantity Dispute",
    "Quantity Dispute",
    "Quantity Dispute",

    "Contract Breach",
    "Contract Breach",
    "Contract Breach"
]


# Train vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train classifier
model = LogisticRegression()
model.fit(X, labels)

# Save model
joblib.dump(vectorizer, "backend/services/vectorizer.pkl")
joblib.dump(model, "backend/services/classifier.pkl")

print("Classifier trained and saved.")
