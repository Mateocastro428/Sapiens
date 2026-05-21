from sqlalchemy import Column, Integer, String
from app.infrastructure.database import Base

class EstadoSesion(Base):
    __tablename__ = "estado_sesion"

    id = Column(Integer, primary_key=True, index=True)

    estado = Column(String)