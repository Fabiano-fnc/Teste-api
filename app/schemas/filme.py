from pydantic import BaseModel
from enum import Enum

class GeneroFilme(str, Enum):
    ACAO = "ACAO"
    HUMOR = "HUMOR"
    TERROR = "TERROR"

class FilmeCreate(BaseModel):  # Schema para criação (SEM ID)
    titulo: str
    genero: GeneroFilme

class Filme(FilmeCreate):  # Schema para resposta (COM ID)
    id: int

    class Config:
        orm_mode = True