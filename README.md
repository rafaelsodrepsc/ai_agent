# Agente Mentor de Programação com IA

## Visão Geral

Este projeto implementa um agente conversacional de IA atuando como **Mentor de Programação técnico e direto**, utilizando:

- Flask (API REST backend)
- Ollama (execução local de modelo LLM)
- Memória de conversa baseada em sessão
- Arquitetura modular (Camada de Serviço + Camada de Memória)
- Interface de chat via terminal (CLI)

O agente foi projetado para orientar usuários com explicações claras, objetivas e estruturadas, incentivando raciocínio técnico.

---

## Arquitetura

```
.
├── app.py                  # Entrada principal da API Flask
├── chat.py                 # Interface de terminal (CLI)
├── agent_config.py         # Configuração do prompt do sistema
├── services/
│   └── llm_service.py      # Camada de integração com o LLM
├── memory/
│   └── session_manager.py  # Gerenciamento de memória por sessão
├── requirements.txt
└── README.md
```

### Camadas

- **Flask (Camada de Controle)** → Gerencia requisições HTTP
- **SessionManager (Camada de Memória)** → Gerencia histórico por sessão
- **LLMService (Camada de Serviço)** → Comunicação com o Ollama
- **System Prompt** → Define identidade e comportamento do agente

---

## Requisitos

- Python 3.10+
- Ollama instalado
- Modelo baixado no Ollama (exemplo: `phi3:mini`)

Instalar modelo:

```bash
ollama pull phi3:mini
```

---

## Instalação

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd ai_agent
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

Ativar (Windows):

```bash
venv\Scripts\activate
```

Ativar (Linux/Mac):

```bash
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Configuração de Ambiente

Criar um arquivo `.env` na raiz do projeto:

```bash
OLLAMA_URL=http://localhost:11434
MODEL_NAME=phi3:mini
```

---

## Executando a Aplicação

### Iniciar o servidor da API

```bash
python app.py
```

O servidor ficará disponível em:

```
http://127.0.0.1:5000
```

---

## Utilizando a Interface de Terminal

Em outro terminal, execute:

```bash
python chat.py
```

Agora você pode conversar diretamente com o Mentor de Programação.

Para encerrar a sessão, digite:

```
exit
```

---

## Endpoint da API

### POST /chat

Requisição:

```json
{
  "session_id": "usuario1",
  "message": "Explique encapsulamento em POO"
}
```

Resposta:

```json
{
  "response": "Encapsulamento é..."
}
```

---

## Funcionalidades

- Isolamento de conversa por sessão
- Controle de histórico com janela deslizante
- Prompt de sistema configurável
- Arquitetura modular e organizada
- Interface de chat via terminal

---

## Limitações

- Histórico armazenado apenas em memória (RAM)
- Não é thread-safe
- Não possui autenticação
- Não recomendado para produção

---

## Melhorias Futuras

- Persistência em banco de dados (Redis/PostgreSQL)
- Controle de contexto baseado em tokens
- Resumo automático de conversas longas
- Respostas com streaming
- Interface web
- Autenticação e suporte multiusuário

---

## Objetivo do Projeto

Este projeto foi desenvolvido para:

- Estudar arquitetura de agentes conversacionais
- Compreender organização modular de backend
- Praticar integração com LLMs locais
- Aprimorar boas práticas de estrutura de software