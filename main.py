from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

from app.interfaces.routers.usuarios import router as usuarios_router
from app.interfaces.routers.course import router as cursos_router
from app.interfaces.routers.lecciones import router as lecciones_router
from app.interfaces.routers.inscripciones import router as inscripciones_router


from app.infrastructure.database import Base, engine

app = FastAPI(title="Sapiens API")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(BASE_DIR, "static")

if not os.path.exists(static_dir):
    raise Exception(f"No existe la carpeta static en: {static_dir}")

# Montar toda la carpeta static en /static (para CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

def servir_html(ruta_relativa: str):
    """Busca el archivo HTML dentro de static_dir"""
    path = os.path.join(static_dir, ruta_relativa)
    if os.path.exists(path):
        return FileResponse(path)
    return {"error": "Archivo no encontrado", "ruta": path}


@app.get("/")
def index():
    return servir_html("index.html")

@app.get("/index.html")
def index_html():
    return servir_html("index.html")

@app.get("/metodologia")
def metodologia():
    return servir_html("metodologia.html")

@app.get("/metodologia.html")
def metodologia_html():
    return servir_html("metodologia.html")

@app.get("/registro")
def registro():
    return servir_html("registro.html")

@app.get("/registro.html")
def registro_html():
    return servir_html("registro.html")

@app.get("/eras")
def eras():
    return servir_html("eras.html")

@app.get("/eras.html")
def eras_html():
    return servir_html("eras.html")

@app.get("/progreso")
def progreso():
    return servir_html("progreso.html")

@app.get("/progreso.html")
def progreso_html():
    return servir_html("progreso.html")

@app.get("/acerca")
def acerca():
    return servir_html("acerca.html")

@app.get("/acerca.html")
def acerca_html():
    return servir_html("acerca.html")

@app.get("/api")
def api_status():
    return {"mensaje": "Sapiens API funcionando 🚀"}


app.include_router(cursos_router)
app.include_router(lecciones_router)
app.include_router(inscripciones_router)
app.include_router(usuarios_router)


Base.metadata.create_all(bind=engine)