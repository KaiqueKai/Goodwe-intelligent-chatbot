import os
from dotenv import load_dotenv
from ollama import Client

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(os.path.join(BASE_DIR, ".env"))

API_KEY = os.getenv("OLLAMA_API_KEY")

client = Client(
    host="https://ollama.com",
    headers={
        "Authorization": f"Bearer {API_KEY}"
    }
)

with open(
    os.path.join(BASE_DIR, "prompts", "system_prompt.md"),
    "r",
    encoding="utf-8"
) as arquivo:
    system_prompt = arquivo.read()

historico = [
    {
        "role": "system",
        "content": system_prompt
    }
]

print("=" * 60)
print("GOODWE INTELLIGENT CHATBOT")
print("=" * 60)
print("Digite 'sair' para encerrar.\n")

while True:

    pergunta = input("Você: ")

    if pergunta.lower() == "sair":
        print("Encerrando chatbot...")
        break

    historico.append(
        {
            "role": "user",
            "content": pergunta
        }
    )

    try:

        resposta = client.chat(
            model="gemma3:4b",
            messages=historico
        )

        resposta_ia = resposta.message.content

        historico.append(
            {
                "role": "assistant",
                "content": resposta_ia
            }
        )

        print("\nChatbot:")
        print(resposta_ia)
        print()

    except Exception as erro:
        print("\nERRO:")
        print(erro)
        print()