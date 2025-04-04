from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Montar carpeta de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Carpeta de templates HTML
templates = Jinja2Templates(directory="templates")

# Ruta principal
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Acá vas a ir agregando más rutas para los formularios
# Ejemplo:
# @app.get("/historia-completa")
# async def historia_completa(request: Request):
#     return templates.TemplateResponse("historia_completa.html", {"request": request})
