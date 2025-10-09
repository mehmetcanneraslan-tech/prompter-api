from fastapi import APIRouter, HTTPException
import requests

router = APIRouter(prefix="/chat", tags=["Chatbot"])

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:4b"

@router.post("/")
def chat_with_ollama(prompt: dict):
    user_input = prompt.get("message")
    if not user_input:
        raise HTTPException(status_code=400, detail="Mesaj boş olamaz.")

    payload = {
        "model": MODEL_NAME,
        "prompt": user_input
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, stream=True)
        result = ""

        for line in response.iter_lines():
            if line:
                data = line.decode("utf-8")
                if '"response"' in data:
                    part = data.split('"response":"')[1].split('"')[0]
                    result += part

        return { result.strip()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
