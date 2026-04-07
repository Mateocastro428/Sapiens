from pydantic import BaseModel, EmailStr

class UsuarioCreate(BaseModel):
    username: str
    email: EmailStr
    password: str



class UsuarioResponse(BaseModel):
    id: int
    username: str
    email: str
    puntos: int
    nivel: int

    class Config:
        from_attributes = True