import re
import spacy


nlp = spacy.load("en_core_web_sm")


def extract_amount(text: str):
    pattern = r"(₹|Rs\.?|INR)\s?([0-9,]+)"
    match = re.search(pattern, text)

    if match:
        return match.group(2).replace(",", "")

    return None


def extract_dates(text: str):
    pattern = r"(\d{2}[-/]\d{2}[-/]\d{4})"
    return re.findall(pattern, text)


def extract_parties(text: str):
    doc = nlp(text)

    orgs = []

    for ent in doc.ents:
        if ent.label_ == "ORG":
            orgs.append(ent.text)

    claimant = orgs[0] if len(orgs) > 0 else None
    respondent = orgs[1] if len(orgs) > 1 else None

    return claimant, respondent


def detect_dispute_type(text: str):

    t = text.lower()

    if "delay" in t or "late" in t:
        return "Delayed Payment"

    if "quality" in t or "defect" in t:
        return "Quality Dispute"

    if "quantity" in t or "short supply" in t:
        return "Quantity Dispute"

    if "breach" in t:
        return "Contract Breach"

    return "General Dispute"


def extract_fields(text: str):

    amount = extract_amount(text)
    dates = extract_dates(text)
    claimant, respondent = extract_parties(text)
    dispute_type = detect_dispute_type(text)

    invoice_date = dates[0] if len(dates) > 0 else None
    due_date = dates[1] if len(dates) > 1 else None

    return {
        "claimant": claimant,
        "respondent": respondent,
        "amount": amount,
        "invoice_date": invoice_date,
        "due_date": due_date,
        "dispute_type": dispute_type
    }
