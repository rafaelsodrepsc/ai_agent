import requests

API_URL = "http://127.0.0.1:5000/chat"
SESSION_ID = "terminal_user"


def main():
    print("Mentor de Programação (modo técnico e direto)")
    print("Digite 'exit' para sair.\n")

    while True:
        user_input = input("Você: ")

        if user_input.lower() in ["exit", "sair", "quit"]:
            print("Encerrando conversa.")
            break

        try:
            response = requests.post(
                API_URL,
                json={
                    "session_id": SESSION_ID,
                    "message": user_input
                },
            )

            response.raise_for_status()

            data = response.json()
            print("\nMentor:", data["response"], "\n")

        except requests.exceptions.RequestException as e:
            print("\nErro ao conectar com o agente:", e, "\n")


if __name__ == "__main__":
    main()
