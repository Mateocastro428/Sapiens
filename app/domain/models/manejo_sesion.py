from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class ManejoSesion(Base):
    __tablename__ = "manejo_sesion"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(Integer, ForeignKey("users.id"))
    estado_id = Column(Integer, ForeignKey("estado_sesion.id"))

    usuario = relationship("User")
    estado = relationship("EstadoSesion")