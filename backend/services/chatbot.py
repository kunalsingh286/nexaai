import ollama


SYSTEM_PROMPT = """
You are NexaAI, an expert legal and negotiation assistant for business disputes.

Your job is to:
- Help recover delayed payments
- Suggest polite but firm responses
- Follow Indian MSME laws
- Avoid giving illegal advice
- Be professional and practical
- Support English and Hindi

Always focus on settlement and resolution.
"""


def chat_with_ai(message: str, history: list = None):

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    if history:
        messages.extend(history)

    messages.append(
        {"role": "user", "content": message}
    )

    response = ollama.chat(
        model="llama3",
        messages=messages
    )

    return response["message"]["content"]
