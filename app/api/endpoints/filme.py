from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...database import get_db
from ...models.filme import Filme as FilmeModel
from ...schemas.filme import FilmeCreate, Filme  # Importe FilmeCreate

router = APIRouter()

@router.post("/filmes/", response_model=Filme)
def criar_filme(filme: FilmeCreate, db: Session = Depends(get_db)):  # Recebe FilmeCreate
    db_filme = FilmeModel(**filme.dict())
    db.add(db_filme)
    db.commit()
    db.refresh(db_filme)
    return db_filme