from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class HistoriaClinica(BaseModel):
    paciente: str
    fecha: str
    motivo: str
    evaluacion: str
    diagnostico: str
    conducta: str
    observaciones: Optional[str] = None
    profesional: str
    matricula: str
    firma: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/receta", response_class=HTMLResponse)
async def receta(request: Request):
    return templates.TemplateResponse("receta.html", {"request": request})


@app.get("/indicaciones", response_class=HTMLResponse)
async def indicaciones(request: Request):
    return templates.TemplateResponse("indicaciones.html", {"request": request})


@app.get("/historia-clinica-completa", response_class=HTMLResponse)
async def historia_clinica_completa(request: Request):
    return templates.TemplateResponse("historia_clinica_completa.html", {"request": request})


@app.get("/historia-clinica-resumida", response_class=HTMLResponse)
async def historia_clinica_resumida(request: Request):
    return templates.TemplateResponse("historia_clinica_resumida.html", {"request": request})


@app.get("/evolucion-diaria", response_class=HTMLResponse)
async def evolucion_diaria(request: Request):
    return templates.TemplateResponse("evolucion_diaria.html", {"request": request})


@app.post("/api/historia-clinica-completa")
async def guardar_historia_completa(data: HistoriaClinica):
    print("Recibido:", data.dict())
    return {"status": "ok", "message": "Historia clínica guardada correctamente"}


@app.get("/status")
def status():
    return {"message": "MEDSYS API activa"}
