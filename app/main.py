from fastapi import FastAPI
from .database import engine, Base  
from .models.usuario import Usuario
from .models.filme import Filme
from .models.review import Review
from .api.endpoints import usuario_router, filme_router, review_router

Base.metadata.create_all(bind=engine)  

app = FastAPI()

app.include_router(usuario_router, prefix="/api")
app.include_router(filme_router, prefix="/api")
app.include_router(review_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "API de Cinema rodando!"}