from pydantic import BaseModel, ConfigDict
from enum import Enum

class GeneroFilme(str, Enum):
    ACAO = "ACAO"
    HUMOR = "HUMOR"
    TERROR = "TERROR"

class FilmeCreate(BaseModel):  
    titulo: str
    genero: GeneroFilme

class Filme(FilmeCreate):  
    id: int

    model_config = ConfigDict(
        from_attributes=True, 
        arbitrary_types_allowed=True
    )