from sqlalchemy import Column, Integer, String
from app.infrastructure.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    puntos = Column(Integer, default=0)
    nivel = Column(Integer, default=1)