from pydantic import BaseModel

class Contenido(BaseModel):
    id: int
    titulo: str
    tipo: str
    publicado: bool
    valoracion: float
    autor: str