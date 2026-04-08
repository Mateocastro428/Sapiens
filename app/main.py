from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.interfaces.routers.usuarios import router as usuarios_router
from app.interfaces.routers.course import router as cursos_router
from app.infrastructure.database import Base, engine
from app.domain.models.user import User
from app.interfaces.routers.lecciones import router as lecciones_router
from app.domain.models.inscripcion import Inscripcion
from app.interfaces.routers.inscripciones import router as inscripciones_router
import os

app = FastAPI(title="Sapiens API")

# Ruta a la carpeta static (un nivel arriba de app)
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def frontend():
    index_path = os.path.join(static_dir, "index.html")
    return FileResponse(index_path)

app.include_router(cursos_router)
app.include_router(lecciones_router)
app.include_router(inscripciones_router)   
app.include_router(usuarios_router)

Base.metadata.create_all(bind=engine)