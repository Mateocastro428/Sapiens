from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class Unidad(Base):
    __tablename__ = "unidades"

    id = Column(Integer, primary_key=True, index=True)
    curso_id = Column(Integer, ForeignKey("cursos.id"))

    titulo = Column(String)
    estado = Column(String)

    curso = relationship("Course")
    lecciones = relationship("Leccion", back_populates="unidad")