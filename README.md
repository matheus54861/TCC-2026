# 🩺 TCC: Benchmark de Inteligência Artificial para Triagem em Fisioterapia Musculoesquelética

Este repositório contém o código-fonte desenvolvido para o Trabalho de Conclusão de Curso (TCC) em Ciência da Computação. O projeto consiste em um **sistema de triagem automatizada baseado em IA** especializado em disfunções da coluna e articulações, utilizando uma arquitetura unificada via **OpenRouter** para comparar o desempenho e a latência de diferentes Modelos de Linguagem (LLMs).

---

## 📁 Estrutura do Projeto

O projeto é modularizado nos seguintes arquivos principais:
- **`main.py`**: Controla o menu interativo de seleção de modelos, o fluxo de conversação com o paciente e o registro de tempo de resposta (latência).
- **`prompt.py`**: Contém as instruções de sistema (*System Prompt*) e a base de conhecimento clínico utilizada para orientar a conduta da IA.
- **`config.py`**: Arquivo de configuração local para armazenamento seguro da chave de API e mapeamento dos modelos (excluído do controle de versão por segurança).
- **`.gitignore`**: Garante a proteção de credenciais sensíveis e evita o rastreio de arquivos temporários e do ambiente virtual.

---

## 🛠️ Tecnologias Utilizadas
- **Python** (Linguagem principal)
- **OpenAI SDK / OpenRouter API** (Orquestração de modelos de IA)
- **Git & GitHub** (Controle de versão e versionamento de código)

---

## ⚙️ Como Executar o Projeto em Qualquer Computador

Para rodar este repositório localmente sem erros, siga os passos abaixo:

### 1. Clonar o Repositório
Abra o terminal na pasta onde deseja guardar o projeto e execute:
```bash
git clone https://github.com/matheus54861/TCC-2026.git
cd TCC-2026

### 2. Criar Arquivo de Configuração (config.py)
Crie um arquivo chamado config.py na raiz do projeto com o seguinte conteúdo:

