# 🩺 TCC: Benchmark de Inteligência Artificial para Triagem em Fisioterapia Musculoesquelética

Este repositório contém o código-fonte desenvolvido para o Trabalho de Conclusão de Curso (TCC) em Ciência da Computação.

O projeto consiste em um **sistema de triagem automatizada baseado em Inteligência Artificial (IA)**, especializado em disfunções da coluna e articulações, utilizando uma arquitetura unificada via **OpenRouter** para comparar o desempenho e a latência de diferentes Modelos de Linguagem (LLMs).

---

## 📁 Estrutura do Projeto

O projeto é modularizado nos seguintes arquivos principais:

- **`main.py`**: Controla o menu interativo de seleção de modelos, o fluxo de conversação com o paciente e o registro do tempo de resposta (latência).
- **`prompt.py`**: Contém as instruções de sistema (*System Prompt*) e a base de conhecimento clínico utilizada para orientar a conduta da IA.
- **`config.py`**: Arquivo de configuração local para armazenamento seguro da chave de API e mapeamento dos modelos. Esse arquivo deve ser excluído do controle de versão por segurança.
- **`.gitignore`**: Garante a proteção de credenciais sensíveis e evita o rastreamento de arquivos temporários e do ambiente virtual.

---

## 🛠️ Tecnologias Utilizadas

- **Python** — Linguagem principal.
- **OpenAI SDK / OpenRouter API** — Orquestração de modelos de Inteligência Artificial.
- **Git & GitHub** — Controle de versão e versionamento de código.

---

## ⚙️ Como Executar o Projeto em Qualquer Computador

Para executar este repositório localmente, siga os passos abaixo:

### 1. Clonar o Repositório

Abra o terminal na pasta onde deseja armazenar o projeto e execute:

```bash
git clone https://github.com/matheus54861/TCC-2026.git
cd TCC-2026
```

### 2. Criar o Arquivo de Configuração (`config.py`)

Crie um arquivo chamado **`config.py`** na raiz do projeto com o seguinte conteúdo:

```python
# config.py

OPENROUTER_API_KEY = "sua-chave-do-openrouter-aqui"

MODELOS = {
    "1": "google/gemini-3.8-flash",
    "2": "meta-llama/llama-3.1-8b-instruct",
    "3": "mistralai/mistral-7b-instruct",
}
```

**Importante:** Substitua `sua-chave-do-openrouter-aqui` pela sua chave de API do OpenRouter. Não compartilhe sua chave e não a envie para o GitHub.

### 3. Configurar o Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto. No Windows, utilizando o PowerShell, execute:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 4. Instalar as Dependências

Com o ambiente virtual ativado, instale a biblioteca necessária para a comunicação com a API:

```bash
pip install openai
```

### 5. Executar o Sistema

Após concluir as configurações e a instalação das dependências, inicie a aplicação com o comando:

```bash
python main.py
```

---

## 🔐 Segurança

Para manter a segurança do projeto:

- Não compartilhe sua chave de API.
- Não envie o arquivo `config.py` para o GitHub.
- Certifique-se de que o arquivo `.gitignore` esteja configurado para ignorar o arquivo `config.py` e a pasta `venv/`.
- Mantenha suas credenciais armazenadas apenas localmente.

---

## 🎓 Trabalho de Conclusão de Curso

Projeto desenvolvido como parte do Trabalho de Conclusão de Curso em **Ciência da Computação**.

**Tema:** Benchmark de Inteligência Artificial para Triagem em Fisioterapia Musculoesquelética.

---
