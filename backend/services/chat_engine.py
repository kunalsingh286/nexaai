import ollama


SYSTEM_PROMPT = """
You are NexaAI, an AI negotiation assistant for business disputes in India.

Rules:
- Be polite and professional
- Give practical advice
- Support Hindi and English
- Follow Indian business law
- Do not suggest illegal actions
"""


def chat_with_user(message: str):

    prompt = f"""
{SYSTEM_PROMPT}

User:
{message}

Assistant:
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    reply = response["message"]["content"]

    return reply
