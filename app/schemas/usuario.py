from pydantic import BaseModel
from uuid import UUID

class UsuarioBase(BaseModel):
    nome: str  # Campo obrigatório

class UsuarioCreate(UsuarioBase):  # Schema para criação
    pass

class Usuario(UsuarioBase):  # Schema para resposta
    id: UUID  # Agora com UUID em vez de int

    class Config:
        orm_mode = True  # Permite conversão automática de ORM para Pydantic
