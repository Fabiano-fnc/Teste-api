# 🎬 Teste API - Cinema FastAPI

API REST feita com **FastAPI**, **PostgreSQL** e **Alembic**, com suporte a migrações e estrutura organizada em módulos.

---

## 🚀 Requisitos

- Python 3.11+
- PostgreSQL
- `virtualenv` ou `venv`

---

## ⚙️ Setup do Projeto

1. Clone o repositório:

  - git clone https://github.com/Fabiano-fnc/Teste-api

2. Crie e ative um ambiente virtual:

  - python -m venv .venv
  - source .venv/bin/activate  # Linux/Mac
  - .venv\Scripts\activate     # Windows

3. Instale as dependências:

  - pip install -r requirements.txt

4. Crie um arquivo .env na raiz com o conteúdo:

  - DATABASE_URL="postgresql://postgres@localhost:5432/cinema_db"



## 🧬 Rodando as Migrations (Alembic)

1. Gere as tabelas com Alembic:

  - alembic upgrade head

 1.2 Se criar ou alterar modelos no futuro:

  - alembic revision --autogenerate -m "mensagem_da_migration"
  -alembic upgrade head

## 🧪 Rodando a API

  python -m uvicorn app.main:app --reload

  - **Acesse: http://localhost:8000**
  - **Docs: http://localhost:8000/docs**

## 🧪 Testes

Para executar os testes automatizados da API:

# Ative o ambiente virtual (se aplicável)
source .venv/bin/activate  # Linux/Mac
# ou 
.\.venv\Scripts\activate   # Windows

# Instale as dependências de testes (caso não tenha feito)
pip install pytest

# Execute todos os testes
pytest

- Saída espeerada:

=========================== test session starts ============================
platform linux -- Python 3.12.3, pytest-8.3.5, pluggy-1.5.0
collected 5 items

tests/test_endpoints.py ....                                          [80%]
tests/test_main.py .                                                  [100%]

============================ 5 passed in 0.40s ============================


## 🗂 Estrutura de Pastas

```bash
.venv/
alembic/
├── versions/
app/
├── api/
│   └── endpoints/
│       ├── filme.py
│       ├── review.py
│       └── usuario.py
├── models/
│   ├── filme.py
│   ├── review.py
│   └── usuario.py
├── schemas/
│   ├── filme.py
│   ├── review.py
│   └── usuario.py
├── database.py
├── main.py
.env
requirements.txt
alembic.ini



## ✍️ Autor

  - @Fabiano-fnc














