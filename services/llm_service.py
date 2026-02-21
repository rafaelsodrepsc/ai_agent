import requests
import os
from dotenv import load_dotenv
from agent_config import SYSTEM_PROMPT

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

class LLMService:
    def generate_response(self, messages):
        messages_with_system = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ] + messages

        payload = {
            "model": MODEL_NAME,
            "messages": messages,
            "stream": False
        }

        response = requests.post(
            f"{OLLAMA_URL}/api/chat",
            json=payload
        )

        response.raise_for_status()

        return response.json()["message"]["content"]