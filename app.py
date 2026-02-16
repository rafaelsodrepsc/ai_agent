from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

app = Flask(__name__)

conversation_history = [
    {"role": "system", "content": "Você é um assistente útil e técnico."}
]

def chamar_modelo_local(messages):
    """
    Envia as mensagens para o PHi3 (rodando localmente)
    e retorna a resposta do modelo.
    """

    response = requests.post(
        f"{OLLAMA_URL}/api/chat",  
        json={
            "model": MODEL_NAME, 
            "messages": messages,
            "stream": False  
        },
    )

    resposta_json = response.json()

    return resposta_json["message"]["content"]

@app.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint que recebe mensagem do usuário
    e retorna resposta do agente.
    """

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON não enviado corretamente"}), 400

    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Mensagem não fornecida"}), 400

    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    system_mensage = conversation_history[0]
    
    recent_msg = conversation_history[1:][-10:]
    
    conversation_history[:] = [system_mensage] + recent_msg

    assistant_reply = chamar_modelo_local(conversation_history)

    conversation_history.append({
        "role": "assistant",
        "content": assistant_reply
    })

    return jsonify({
        "response": assistant_reply
    })

if __name__ == "__main__":
    app.run(debug=True)
