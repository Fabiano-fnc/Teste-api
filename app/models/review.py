from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..database import Base

class Review(Base):
    __tablename__ = "review"

    id_usuario = Column(UUID(as_uuid=True), ForeignKey("usuario.id"), primary_key=True)
    id_filme = Column(Integer, ForeignKey("filme.id"), primary_key=True)
    estrelas = Column(Integer, nullable=False)
    
    # Relações
    usuario = relationship("Usuario", back_populates="reviews")
    filme = relationship("Filme", back_populates="reviews")