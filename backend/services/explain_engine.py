import joblib
import numpy as np


class ExplainEngine:

    def explain_risk(self, input_data):

        features = [
            "dispute_type",
            "amount",
            "delay_days",
            "doc_length",
            "sentiment",
            "legal_strength"
        ]

        weights = {
            "amount": 0.25,
            "delay_days": 0.2,
            "legal_strength": 0.2,
            "sentiment": 0.15,
            "doc_length": 0.1,
            "dispute_type": 0.1
        }

        explanation = []

        for f in features:

            val = input_data.get(f, 0)
            impact = round(val * weights[f], 3)

            explanation.append({
                "feature": f,
                "value": val,
                "impact_score": impact
            })

        explanation = sorted(
            explanation,
            key=lambda x: abs(x["impact_score"]),
            reverse=True
        )

        return explanation


engine = ExplainEngine()
