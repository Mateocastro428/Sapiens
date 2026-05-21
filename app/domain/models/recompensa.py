from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class Recompensa(Base):
    __tablename__ = "recompensas"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(Integer, ForeignKey("users.id"))

    nombre = Column(String)
    fecha = Column(String)

    usuario = relationship("User")