from sqlalchemy import Column, Integer, String, ForeignKey
from app.infrastructure.database import Base

class Leccion(Base):
    __tablename__ = "lecciones"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    contenido = Column(String)

    curso_id = Column(Integer, ForeignKey("cursos.id"))