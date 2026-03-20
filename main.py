from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers.usuarios import router as usuarios_router
from routers.contenidos import router as contenidos_router

app = FastAPI(title="Sapiens API")

app.include_router(usuarios_router)
app.include_router(contenidos_router)

@app.get("/")
def inicio():
    return RedirectResponse(url="/docs")