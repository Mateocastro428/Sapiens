from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class Respuesta(Base):
    __tablename__ = "respuestas"

    id = Column(Integer, primary_key=True, index=True)

    tema_id = Column(Integer, ForeignKey("temas.id"))

    contenido = Column(String)

    tema = relationship("Tema", back_populates="respuestas")