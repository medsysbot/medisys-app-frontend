from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import RedirectResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Pantalla principal
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# ENDPOINTS simulados
@app.post("/generate")
async def generate_document(request: Request):
    return {"status": "ok"}

@app.post("/historia_completa")
async def historia_completa(request: Request):
    return {"status": "historia_completa recibida"}

@app.post("/historia_resumida")
async def historia_resumida(request: Request):
    return {"status": "historia_resumida recibida"}

@app.post("/evolucion")
async def evolucion(request: Request):
    return {"status": "evolución recibida"}

@app.post("/receta")
async def receta(request: Request):
    return {"status": "receta recibida"}

@app.post("/indicaciones")
async def indicaciones(request: Request):
    return {"status": "indicaciones recibidas"}
