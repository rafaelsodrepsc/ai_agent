from flask import Flask, request, jsonify
from memory.session_manager import SessionManager
from services.llm_service import LLMService

app = Flask(__name__)

session_manager = SessionManager()
llm_service = LLMService()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    session_id = data.get("session_id")
    user_message = data.get("message")

    if not session_id or not user_message:
        return jsonify({"error": "session_id and message are required"}), 400

    session_manager.add_message(session_id, "user", user_message)

    history = session_manager.get_history(session_id)

    try:
        assistant_reply = llm_service.generate_response(history)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    session_manager.add_message(session_id, "assistant", assistant_reply)

    return jsonify({"response": assistant_reply})


if __name__ == "__main__":
    app.run(debug=True)