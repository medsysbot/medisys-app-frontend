from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("inicio.html", {"request": request})

@app.get("/registro", response_class=HTMLResponse)
async def registro(request: Request):
    return templates.TemplateResponse("registro.html", {"request": request})

@app.get("/historia", response_class=HTMLResponse)
async def historia(request: Request):
    return templates.TemplateResponse("historia.html", {"request": request})

@app.get("/recetas", response_class=HTMLResponse)
async def recetas(request: Request):
    return templates.TemplateResponse("recetas.html", {"request": request})

@app.get("/indicaciones", response_class=HTMLResponse)
async def indicaciones(request: Request):
    return templates.TemplateResponse("indicaciones.html", {"request": request})

@app.get("/turnos", response_class=HTMLResponse)
async def turnos(request: Request):
    return templates.TemplateResponse("turnos.html", {"request": request})
