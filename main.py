from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

from app.interfaces.routers.pages import router as pages_router
from app.interfaces.routers.usuarios import router as usuarios_router
from app.interfaces.routers.course import router as cursos_router
from app.interfaces.routers.lecciones import router as lecciones_router
from app.interfaces.routers.inscripciones import router as inscripciones_router
from app.interfaces.routers.auth import router as auth_router
from app.infrastructure.database import Base, engine

app = FastAPI(title="Sapiens API")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(BASE_DIR, "static")

if not os.path.exists(static_dir):
    raise Exception(f"No existe la carpeta static en: {static_dir}")

# Montar toda la carpeta static en /static (para CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/api")
def api_status():
    return {"mensaje": "Sapiens API funcionando 🚀"}

app.include_router(pages_router)
app.include_router(cursos_router)
app.include_router(lecciones_router)
app.include_router(inscripciones_router)
app.include_router(usuarios_router)
app.include_router(auth_router)

from app.domain.models.unidad import Unidad
from app.domain.models.ejercicio import Ejercicio
from app.domain.models.gamificacion import Progreso, Intento, Habilidad, Logro, Recompensa, Vida
from app.domain.models.estado_sesion import EstadoSesion
from app.domain.models.manejo_sesion import ManejoSesion
from app.domain.models.foro import Foro
from app.domain.models.tema import Tema
from app.domain.models.respuesta import Respuesta
Base.metadata.create_all(bind=engine)