from pydantic import BaseModel, ConfigDict
from uuid import UUID

class UsuarioBase(BaseModel):
    nome: str 

class UsuarioCreate(UsuarioBase): 
    pass

class Usuario(UsuarioBase):  
    id: UUID  

    model_config = ConfigDict(
        from_attributes=True,  
        arbitrary_types_allowed=True
    )  
