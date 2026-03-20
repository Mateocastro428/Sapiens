from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    username: str
    email: str
    password: str
    puntos: int = 0