from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class Leccion(Base):
    __tablename__ = "lecciones"

    id = Column(Integer, primary_key=True, index=True)

    titulo = Column(String)
    contenido = Column(String)

    curso_id = Column(Integer, ForeignKey("cursos.id"))
    unidad_id = Column(Integer, ForeignKey("unidades.id"))

    curso = relationship("Course")
    unidad = relationship("Unidad", back_populates="lecciones")

    ejercicios = relationship("Ejercicio", back_populates="leccion")