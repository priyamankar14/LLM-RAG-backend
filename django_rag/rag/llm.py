import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3:mini"


def generate_answer(context: str, question: str) -> str:
    prompt = f"""
You are a helpful AI assistant.
Answer ONLY from the provided context. If the answer is not in the context, say: "No relevant documents found."
Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=120)
    response.raise_for_status()

    return response.json()["response"].strip()
