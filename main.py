from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers.usuarios import router as usuarios_router
from routers.contenidos import router as contenidos_router
from routers.gamificacion import router as gamificacion_router
from routers.comunidad import router as comunidad_router

app = FastAPI(title="Sapiens API")

app.include_router(usuarios_router)
app.include_router(contenidos_router)
app.include_router(gamificacion_router)
app.include_router(comunidad_router)

@app.get("/")
def inicio():
    return RedirectResponse(url="/docs")