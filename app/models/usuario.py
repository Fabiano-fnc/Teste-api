from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    nome = Column(String(100), nullable=False, unique=True)
    
    reviews = relationship("Review", back_populates="usuario")