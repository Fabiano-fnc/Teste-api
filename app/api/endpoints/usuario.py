from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session  # Adicione esta linha
from ...database import get_db
from ...models.usuario import Usuario  # Import absoluto
from ...schemas.usuario import UsuarioCreate  # Import absoluto

router = APIRouter()

@router.post("/usuarios/")
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = Usuario(nome=usuario.nome)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario