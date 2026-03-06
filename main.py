from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from login.login import router as login_router

app = FastAPI()

app.include_router(login_router)

@app.get("/")
def inicio():
    return RedirectResponse(url="/registro")