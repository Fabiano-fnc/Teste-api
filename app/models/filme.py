from sqlalchemy import Column, Integer, String, Enum as SqlEnum
from sqlalchemy.orm import relationship
from ..database import Base
from enum import Enum  

class GeneroFilme(str, Enum):  
    ACAO = "ACAO"
    HUMOR = "HUMOR"
    TERROR = "TERROR"

class Filme(Base):
    __tablename__ = "filme"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    genero = Column(SqlEnum(GeneroFilme), nullable=False)  
    
    reviews = relationship("Review", back_populates="filme")
