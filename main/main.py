from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI(
    title="Sapiens API",
    description="Bienvenido a aprender con Sapiens 🚀"
)

@app.get("/")
def home():
    return {"mensaje": "👋 Bienvenido a aprender con Sapiens"}

class Usuario(BaseModel):
    nombre: str
    edad: int
    correo: EmailStr

@app.post("/registro")
def registrar_usuario(usuario: Usuario):
    if not usuario.nombre.strip():
        return {"error": "El nombre no puede estar vacío"}
    if usuario.edad <= 0 or usuario.edad > 120:
        return {"error": "Edad inválida"}
    return {"mensaje": f"¡Bienvenido {usuario.nombre} a Sapiens!", "usuario": usuario}

@app.get("/usuarios/{nombre}")
def obtener_usuario(nombre: str):
    return {"nombre": nombre, "edad": 30, "correo": "ejemplo@correo.com"}

@app.delete("/usuarios/{nombre}")
def eliminar_usuario(nombre: str):
    return {"mensaje": f"Usuario {nombre} eliminado correctamente"}
