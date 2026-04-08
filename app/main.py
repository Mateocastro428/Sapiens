from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.interfaces.routers.usuarios import router as usuarios_router
from  app.interfaces.routers.course import router as cursos_router
from app.infrastructure.database import Base, engine
from app.domain.models.user import User
from app.interfaces.routers.lecciones import router as lecciones_router


app = FastAPI(title="Sapiens API")
app.include_router(cursos_router)
app

Base.metadata.create_all(bind=engine)

app.include_router(usuarios_router)

@app.get("/")
def inicio():
    return RedirectResponse(url="/docs")