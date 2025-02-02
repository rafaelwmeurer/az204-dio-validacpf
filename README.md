# API Validador de CPF

API simples para validação de CPF desenvolvida em Python, pronta para execução local e deploy no Azure Functions.

## 📋 Características

- Validação completa de CPF seguindo todas as regras oficiais
- Suporte para execução local via Docker ou Python direto
- Configurado para deploy no Azure Functions
- Inclui testes unitários
- API REST com FastAPI

## 🚀 Começando

### Pré-requisitos

- Python 3.11+
- Docker e Docker Compose (opcional)
- Azure Functions Core Tools (para deploy)

### 📦 Estrutura do Projeto

```
.
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── host.json
├── local.settings.json
├── function_app.py
└── tests
    └── test_cpf_validator.py
```

### 🔧 Instalação e Execução

#### Opção 1: Usando Docker

```bash
# Clone o repositório
git clone 
cd 

# Execute com Docker Compose
docker-compose up --build
```

#### Opção 2: Usando Python diretamente

```bash
# Clone o repositório
git clone 
cd 

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
uvicorn function_app:app --host 0.0.0.0 --port 7071
```

### 🔍 Testando a API

A API estará disponível em `http://localhost:7071`

#### Exemplo de requisição usando curl:

```bash
curl -X POST http://localhost:7071/api/validate-cpf \
-H "Content-Type: application/json" \
-d '{"cpf": "529.982.247-25"}'
```

#### Resposta esperada:

```json
{
    "is_valid": true
}
```

### ⚡ Executando os Testes

```bash
pytest tests/
```

## 📤 Deploy no Azure Functions

1. Instale o Azure Functions Core Tools
2. Configure sua conta Azure
3. Execute:
```bash
func azure functionapp publish 
```

## 🔒 Validação do CPF

A API implementa as seguintes regras de validação:
- Verifica se possui 11 dígitos
- Remove caracteres especiais (pontos e traços)
- Valida se não são todos números iguais
- Aplica o algoritmo oficial de validação dos dígitos verificadores

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Azure Functions](https://azure.microsoft.com/services/functions/)
- [Docker](https://www.docker.com/)
- [pytest](https://docs.pytest.org/)

## ✒️ Autores

* **Rafael Wessling Meurer** - *Desenvolvimento Inicial* - [rafaelwmeurer](https://github.com/rafaelwmeurer)

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes
