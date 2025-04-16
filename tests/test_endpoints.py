import sys
import os
from uuid import UUID
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_criar_usuario():
    response = client.post("/api/usuarios/", json={"nome": "João"})
    assert response.status_code == 200
    assert "id" in response.json()  # Agora verifica se o UUID foi retornado
    assert isinstance(UUID(response.json()["id"]), UUID)  # Valida se é um UUID válido

def test_criar_filme():
    data = {
        "titulo": "Filme Teste",
        "genero": "ACAO"  # Campo obrigatório no schema
    }
    response = client.post("/api/filmes/", json=data)
    assert response.status_code == 200
    assert response.json()["titulo"] == "Filme Teste"
    assert response.json()["id"] > 0  # ID deve ser um inteiro positivo

def test_criar_review():
    # Primeiro cria um usuário e um filme para referenciar
    usuario = client.post("/api/usuarios/", json={"nome": "Maria"}).json()
    filme = client.post("/api/filmes/", json={"titulo": "Outro Filme", "genero": "TERROR"}).json()

    # Agora cria a review (usando "estrelas" em vez de "nota")
    review_data = {
        "id_usuario": usuario["id"],
        "id_filme": filme["id"],
        "estrelas": 4  # Campo corrigido para "estrelas"
    }
    response = client.post("/api/reviews/", json=review_data)
    assert response.status_code == 200
    assert response.json()["estrelas"] == 4  # Verifica o campo correto

def test_listar_reviews():
    response = client.get("/api/reviews/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)