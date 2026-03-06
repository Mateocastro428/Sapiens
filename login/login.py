from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from exceptions import NombreInvalidoError, EdadInvalidaError, CorreoInvalidoError

app = FastAPI()

class Usuario(BaseModel):
    nombre: str
    edad: int
    correo: EmailStr

def validar_usuario(usuario: Usuario):
    if not usuario.nombre.strip():
        raise NombreInvalidoError("El nombre no puede estar vacío")
    if usuario.edad <= 0 or usuario.edad > 120:
        raise EdadInvalidaError("La edad debe estar entre 1 y 120")
    if not usuario.correo:
        raise CorreoInvalidoError("El correo no puede estar vacío")

@app.post("/registro")
def registrar_usuario(usuario: Usuario):
    validar_usuario(usuario)
    return {"mensaje": "Usuario registrado correctamente", "usuario": usuario}

@app.get("/usuarios/{nombre}")
def obtener_usuario(nombre: str):
    if not nombre.strip():
        raise NombreInvalidoError("El nombre no puede estar vacío")
    return {"nombre": nombre, "edad": 30, "correo": "ejemplo@correo.com"}

@app.delete("/usuarios/{nombre}")
def eliminar_usuario(nombre: str):
    if not nombre.strip():
        raise NombreInvalidoError("El nombre no puede estar vacío")
    return {"mensaje": f"Usuario {nombre} eliminado correctamente"}