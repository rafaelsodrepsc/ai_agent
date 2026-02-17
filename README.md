# Agente de IA com Flask e Ollama

## Descrição

Este projeto implementa um agente de IA utilizando:

- Flask para criação de uma API REST
- Ollama para execução local de um modelo LLM
- Controle básico de histórico de conversa

O sistema recebe mensagens via requisição HTTP, envia o histórico para o modelo local e retorna a resposta gerada.

---

## Requisitos

- Python 3.10+
- Ollama instalado
- Modelo baixado no Ollama (ex: `phi3:mini`)

---

## Instalação

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd nome-do-projeto
```
### 2\. Criar ambiente virtual

```bash
python -m venv venv
```

Ativar no Windows:

```bash
venv\Scripts\activate
```

Ativar no Linux/Mac:

```bash
source venv/bin/activate
```

### 3\. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Configuração

Criar um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```bash
OLLAMA_URL=http://localhost:11434
MODEL_NAME=phi3:mini
```

Certifique-se de que o modelo está instalado:

```bash
ollama pull phi3:mini
```

---

## Execução

Iniciar o servidor:

```bash
python app.py
```

A API ficará disponível em:

```bash
http://127.0.0.1:5000
```

---

## Uso

### Endpoint

```bash
POST /chat
```

### Exemplo de requisição (JSON)

```json
{
  "message": "Explique o que é um agente de IA"
}
```

### Exemplo de resposta

```json
{
  "response": "..."
}
```

---

## Estrutura do Projeto

```bash
.
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## Observações

- O histórico da conversa é mantido em memória.
- A aplicação não implementa isolamento por múltiplos usuários.
