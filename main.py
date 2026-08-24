import os
from dotenv import load_dotenv
from google import genai

# le o arquivo .env e carrega as variaveis dele (no caso, a chave da api)
load_dotenv()

#pegando a chave da api 
client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

print("=" * 50)
print("CHATBOT INICIADO")
print("Digite 'sair para encerrar")
print("=" * 50)

# criar historico vazio
historico = []

# inicia o loop do programa

while True:
    pergunta = input("\nVocê: ")

    # encerrando programa
    if pergunta.lower() == "sair":
        print("\nChat encerrado.")
        break
    #adicionando as perguntas no histórico
    historico.append(
        {
            "role": "user",
            "parts": [{"text": pergunta}]
        }
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=historico
        )

        resposta = response.text   

        print(f"\nChat: {resposta}")

        historico.append(
            {
                "role": "user",
                "parts": [{"text": resposta}]
            }
        )
    
    except Exception as erro:
        print(f"\nErro: {erro}")