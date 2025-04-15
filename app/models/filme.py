from sqlalchemy import Column, Integer, String, Enum as SqlEnum
from sqlalchemy.orm import relationship
from ..database import Base
from enum import Enum  # Enum do Python padrão

class GeneroFilme(str, Enum):  # Agora está certo
    ACAO = "ACAO"
    HUMOR = "HUMOR"
    TERROR = "TERROR"

class Filme(Base):
    __tablename__ = "filme"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    genero = Column(SqlEnum(GeneroFilme), nullable=False)  # Corrigido para SqlEnum
    
    reviews = relationship("Review", back_populates="filme")
