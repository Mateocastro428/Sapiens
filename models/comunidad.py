from pydantic import BaseModel

class Amistad(BaseModel):
    id: int
    usuario_id: int
    amigo_id: int

class Mensaje(BaseModel):
    id: int
    emisor_id: int
    receptor_id: int
    contenido: str