from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class Progreso(Base):
    __tablename__ = "progreso"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(Integer, ForeignKey("users.id"))
    leccion_id = Column(Integer, ForeignKey("lecciones.id"))

    porcentaje_completado = Column(Float)

    usuario = relationship("User")
    leccion = relationship("Leccion")