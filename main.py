import sys
import time
from openai import OpenAI
from config import OPENROUTER_API_KEY, MODELOS
from prompt import SYSTEM_PROMPT

print("=" * 60)
print("TCC - BENCHMARK DE APIS DE TRIAGEM FISIOTERÁPICA (OPENROUTER)")
print("=" * 60)

# ESCOLHA DA INTELIGÊNCIA ARTIFICIAL PELO MENU
print("\nEscolha qual Inteligência Artificial deseja testar:")
print("1 - Google Gemini")
print("2 - Meta Llama")
print("3 - Mistral 7B")

escolha = input("\nDigite o número da opção desejada (1, 2 ou 3): ").strip()

if escolha not in MODELOS:
  print("\n Opção inválida. Reinicie o programa.")
  sys.exit()

modelo_usado = MODELOS[escolha]

# Inicializa o cliente único do OpenRouter
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=OPENROUTER_API_KEY)

print(f"\n Benchmark iniciado com o modelo: {modelo_usado}")
print("Digite 'sair' a qualquer momento para encerrar.")
print("-" * 60)
print()

print(
    "Assistente: Olá! Sou seu assistente de triagem em fisioterapia"
    " musculoesquelética. Qual é a sua principal queixa ou dor no"
    " momento?\n"
)
print("-" * 60)

# Histórico estruturado no formato padrão de mensagens de chat
mensagens = [{"role": "system", "content": SYSTEM_PROMPT}]

while True:
  try:
    texto_usuario = input("Você (Paciente): ")

    if not texto_usuario.strip():
      continue

    if texto_usuario.strip().lower() in ["sair", "exit", "parar"]:
      print("\n Assistente: Atendimento encerrado. Bom benchmark para o TCC!")
      break

    # Adiciona a fala do usuário ao histórico de conversas
    mensagens.append({"role": "user", "content": texto_usuario})

    print("\n Processando...")
    inicio_tempo = time.time()

    # Chamada unificada para o OpenRouter utilizando o cliente OpenAI
    chat_completion = client.chat.completions.create(
        model=modelo_usado, messages=mensagens, temperature=0.1
    )

    texto_resposta = chat_completion.choices[0].message.content

    fim_tempo = time.time()
    tempo_decorrido = round(fim_tempo - inicio_tempo, 2)

    print(
        f"\n Assistente ({modelo_usado} - {tempo_decorrido}s):\n{texto_resposta}\n"
    )
    print("-" * 60)

    # Adiciona a resposta da IA ao histórico de conversas
    mensagens.append({"role": "assistant", "content": texto_resposta})

  except KeyboardInterrupt:
    print("\n\n Atendimento interrompido.")
    break
  except Exception as e:
    print(f"\n Erro na API do OpenRouter: {str(e)}\n")