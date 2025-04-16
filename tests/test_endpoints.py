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
    assert "id" in response.json()  
    assert isinstance(UUID(response.json()["id"]), UUID)  

def test_criar_filme():
    data = {
        "titulo": "Filme Teste",
        "genero": "ACAO"  
    }
    response = client.post("/api/filmes/", json=data)
    assert response.status_code == 200
    assert response.json()["titulo"] == "Filme Teste"
    assert response.json()["id"] > 0  

def test_criar_review():
    usuario = client.post("/api/usuarios/", json={"nome": "Maria"}).json()
    filme = client.post("/api/filmes/", json={"titulo": "Outro Filme", "genero": "TERROR"}).json()

    review_data = {
        "id_usuario": usuario["id"],
        "id_filme": filme["id"],
        "estrelas": 4  
    }
    response = client.post("/api/reviews/", json=review_data)
    assert response.status_code == 200
    assert response.json()["estrelas"] == 4  

def test_listar_reviews():
    response = client.get("/api/reviews/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)