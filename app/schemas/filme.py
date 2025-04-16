from pydantic import BaseModel, ConfigDict
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

    model_config = ConfigDict(
        from_attributes=True,  # substitui orm_mode
        arbitrary_types_allowed=True
    )