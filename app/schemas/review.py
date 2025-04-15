from pydantic import BaseModel, Field
from uuid import UUID
from .usuario import Usuario
from .filme import Filme

class ReviewBase(BaseModel):
    id_usuario: UUID  # CORRIGIDO de str → UUID
    id_filme: int
    estrelas: int = Field(ge=0, le=5)

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    usuario: Usuario
    filme: Filme

    class Config:
        orm_mode = True
