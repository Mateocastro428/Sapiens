from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.interfaces.routers.usuarios import router as usuarios_router
from  app.interfaces.routers.course import router as cursos_router
from app.infrastructure.database import Base, engine
from app.domain.models.user import User
from app.interfaces.routers.lecciones import router as lecciones_router
from app.domain.models.inscripcion import Inscripcion
from app.interfaces.routers.inscripciones import router as inscripciones_router
app = FastAPI(title="Sapiens API")
app.include_router(cursos_router)
app.include_router(lecciones_router)
app.include_router(inscripciones_router)   
 

Base.metadata.create_all(bind=engine)

app.include_router(usuarios_router)

@app.get("/")
def inicio():
    return RedirectResponse(url="/docs")