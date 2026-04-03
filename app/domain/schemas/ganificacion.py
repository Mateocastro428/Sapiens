from pydantic import Basemodel

class Logro(Basemodel):
    id: int
    nombre: str
    descripcion: str
    puntos_requeridos: int

class Nivel(Basemodel):
    nivel: int
    nombre: str
    puntos_minimos: int