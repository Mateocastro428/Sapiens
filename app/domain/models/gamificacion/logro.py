from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class Logro(Base):
    __tablename__ = "logros"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(Integer, ForeignKey("users.id"))

    titulo = Column(String)
    fecha = Column(String)

    usuario = relationship("User")