from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class Tema(Base):
    __tablename__ = "temas"

    id = Column(Integer, primary_key=True, index=True)

    foro_id = Column(Integer, ForeignKey("foro.id"))

    titulo = Column(String)

    foro = relationship("Foro", back_populates="temas")
    respuestas = relationship("Respuesta", back_populates="tema")