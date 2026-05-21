from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class Intento(Base):
    __tablename__ = "intentos"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(Integer, ForeignKey("users.id"))
    ejercicio_id = Column(Integer, ForeignKey("ejercicios.id"))

    validacion_respuesta = Column(String)
    fecha = Column(String)
    tiempo = Column(String)

    usuario = relationship("User")
    ejercicio = relationship("Ejercicio")