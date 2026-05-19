from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class Habilidad(Base):
    __tablename__ = "habilidades"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(Integer, ForeignKey("users.id"))

    nivel = Column(Integer)

    usuario = relationship("User")