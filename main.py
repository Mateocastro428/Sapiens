from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Sapiens API")

# Forzar la ruta absoluta para evitar errores de ubicación
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(BASE_DIR, "static")

if not os.path.exists(static_dir):
    os.makedirs(static_dir)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def frontend():
    index_path = os.path.join(static_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"error": "index.html no encontrado en static/"}

# Importaciones opcionales (comentadas por si los módulos no existen aún)
try:
    from app.interfaces.routers.usuarios import router as usuarios_router
    app.include_router(usuarios_router)
    from app.infrastructure.database import Base, engine
    Base.metadata.create_all(bind=engine)
except ImportError as e:
    print(f"Aviso: No se pudieron cargar módulos de BD/Routers: {e}")

