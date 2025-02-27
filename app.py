from fastapi import FastAPI
import requests

app = FastAPI()

OLLAMA_URL = "http://self-hosted-ollama-llm:11434"

@app.get("/chat")
def chat(query: str):
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={"model": "llama3", "prompt": query},
    )
    return response.json()
