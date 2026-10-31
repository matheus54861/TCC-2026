import sys
import time
from config import CHAVES_API
from prompt import SYSTEM_PROMPT

print("=" * 60)
print("TCC - BENCHMARK DE APIS DE TRIAGEM FISIOTERÁPICA")
print("=" * 60)

# ESCOLHA DA API
print("\nEscolha qual Inteligência Artificial deseja testar:")
print("1 - Google Gemini (gemini-3.8-flash)")
print("2 - Groq API (Llama nativo na Groq)")
print("3 - OpenRouter (Mistral 7B Instruct - Arquitetura Mistral)")

escolha = input("\nDigite o número da opção desejada (1, 2 ou 3): ").strip()

provedor_escolhido = ""
client = None
modelo_usado = ""

if escolha == "1":
    provedor_escolhido = "gemini"
    from google import genai
    client = genai.Client(api_key=CHAVES_API["gemini"])
    modelo_usado = "gemini-3.8-flash"

elif escolha == "2":
    provedor_escolhido = "groq"
    from openai import OpenAI
    client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=CHAVES_API["groq"]
    )
    modelo_usado = "openai/gpt-oss-20b"

elif escolha == "3":
    provedor_escolhido = "openrouter"
    from openai import OpenAI
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=CHAVES_API["openrouter"]
    )
    modelo_usado = "mistralai/mistral-7b-instruct:free"

else:
    print("\n Opção inválida. Reinicie o programa.")
    sys.exit()

print(f"\n Benchmark iniciado com: {provedor_escolhido.upper()} ({modelo_usado})")
print("Digite 'sair' a qualquer momento para encerrar.")
print("-" * 60)
print()

print("Assistente: Olá! Sou seu assistente de triagem em fisioterapia musculoesquelética. Qual é a sua principal queixa ou dor no momento?\n")
print("-" * 60)

historico_conversa = ""

while True:
    try:
        texto_usuario = input("Você (Paciente): ")
        
        if not texto_usuario.strip():
            continue
            
        if texto_usuario.strip().lower() in ['sair', 'exit', 'parar']:
            print("\n Assistente: Atendimento encerrado. Bom benchmark para o TCC!")
            break
            
        prompt_atual = f"""
{SYSTEM_PROMPT}

Histórico recente:
{historico_conversa}

Paciente: {texto_usuario}
Assistente:
"""
        
        print("\n Processando...")
        inicio_tempo = time.time()
        texto_resposta = ""

        # Execução baseada na API escolhida
        if provedor_escolhido == "gemini":
            modelos_para_tentar = ["gemini-3.8-flash", "gemini-2.0-flash", "gemini-1.5-flash"]
            sucesso = False
            for m in modelos_para_tentar:
                try:
                    resposta = client.models.generate_content(
                        model=m,
                        contents=prompt_atual,
                        config={"temperature": 0.1}
                    )
                    texto_resposta = resposta.text
                    sucesso = True
                    break
                except Exception as e:
                    if "404" in str(e) or "NOT_FOUND" in str(e):
                        continue
                    raise e
            if not sucesso:
                raise Exception("Nenhum modelo do Gemini respondeu.")

        elif provedor_escolhido in ["groq", "openrouter"]:
            chat_completion = client.chat.completions.create(
                model=modelo_usado,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": f"Histórico recente:\n{historico_conversa}\n\nPaciente: {texto_usuario}"}
                ],
                temperature=0.1
            )
            texto_resposta = chat_completion.choices[0].message.content

        fim_tempo = time.time()
        tempo_decorrido = round(fim_tempo - inicio_tempo, 2)

        print(f"\n Assistente ({modelo_usado} - {tempo_decorrido}s):\n{texto_resposta}\n")
        print("-" * 60)
        
        historico_conversa += f"\nPaciente: {texto_usuario}\nAssistente: {texto_resposta}"
        
    except KeyboardInterrupt:
        print("\n\n Atendimento interrompido.")
        break
    except Exception as e:
        print(f"\n Erro na API escolhida: {str(e)}\n")