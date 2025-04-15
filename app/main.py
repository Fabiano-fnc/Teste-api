from fastapi import FastAPI
from .database import engine, Base  # Importe Base do database.py
from .models.usuario import Usuario
from .models.filme import Filme
from .models.review import Review
from .api.endpoints import usuario_router, filme_router, review_router

# Cria TODAS as tabelas de uma vez (isso evita erros de dependência)
Base.metadata.create_all(bind=engine)  # Use Base em vez de modelos individuais

app = FastAPI()

# Inclui os routers
app.include_router(usuario_router, prefix="/api")
app.include_router(filme_router, prefix="/api")
app.include_router(review_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "API de Cinema rodando!"}