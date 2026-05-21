from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class Foro(Base):
    __tablename__ = "foro"

    id = Column(Integer, primary_key=True, index=True)

    nombre = Column(String)
    descripcion = Column(String)

    temas = relationship("Tema", back_populates="foro")