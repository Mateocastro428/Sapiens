from sqlalchemy import Column, Integer, ForeignKey
from app.infrastructure.database import Base

class Inscripcion(Base):
    __tablename__ = "inscripciones"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("users.id"))
    curso_id = Column(Integer, ForeignKey("cursos.id"))