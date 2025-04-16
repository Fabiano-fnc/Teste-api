from pydantic import BaseModel, ConfigDict
from uuid import UUID

class UsuarioBase(BaseModel):
    nome: str  # Campo obrigatório

class UsuarioCreate(UsuarioBase):  # Schema para criação
    pass

class Usuario(UsuarioBase):  # Schema para resposta
    id: UUID  # Agora com UUID em vez de int

    model_config = ConfigDict(
        from_attributes=True,  # substitui orm_mode
        arbitrary_types_allowed=True
    )  # Permite conversão automática de ORM para Pydantic
