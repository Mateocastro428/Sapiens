from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class Vida(Base):
    __tablename__ = "vidas"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(Integer, ForeignKey("users.id"))

    vidas_actuales = Column(Integer)
    tiempo_recarga = Column(Integer)

    usuario = relationship("User")