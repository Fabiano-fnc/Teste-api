from pydantic import BaseModel, Field, ConfigDict
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

    model_config = ConfigDict(
        from_attributes=True,  # substitui orm_mode
        arbitrary_types_allowed=True
    )
