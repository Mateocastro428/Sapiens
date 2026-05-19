from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class Ejercicio(Base):
    __tablename__ = "ejercicios"

    id = Column(Integer, primary_key=True, index=True)

    leccion_id = Column(Integer, ForeignKey("lecciones.id"))

    tipo = Column(String)
    contenido = Column(String)
    respuesta_correcta = Column(String)

    leccion = relationship("Leccion")