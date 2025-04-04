from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/historia_clinica", response_class=HTMLResponse)
async def historia_clinica(request: Request):
    return templates.TemplateResponse("historia_completa.html", {"request": request})

@app.get("/evolucion", response_class=HTMLResponse)
async def evolucion(request: Request):
    return templates.TemplateResponse("evolucion.html", {"request": request})

@app.get("/historia_resumida", response_class=HTMLResponse)
async def historia_resumida(request: Request):
    return templates.TemplateResponse("historia_resumida.html", {"request": request})

@app.get("/recetas", response_class=HTMLResponse)
async def recetas(request: Request):
    return templates.TemplateResponse("receta.html", {"request": request})

@app.get("/indicaciones", response_class=HTMLResponse)
async def indicaciones(request: Request):
    return templates.TemplateResponse("indicaciones.html", {"request": request})
