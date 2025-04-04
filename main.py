from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Monta los archivos estáticos (CSS, imágenes, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define carpeta de templates
templates = Jinja2Templates(directory="templates")

# Ruta de inicio
@app.get("/", response_class=HTMLResponse)
async def inicio(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Vistas individuales
@app.get("/historia_completa", response_class=HTMLResponse)
async def historia_completa(request: Request):
    return templates.TemplateResponse("historia_completa.html", {"request": request})

@app.get("/historia_resumida", response_class=HTMLResponse)
async def historia_resumida(request: Request):
    return templates.TemplateResponse("historia_resumida.html", {"request": request})

@app.get("/evolucion", response_class=HTMLResponse)
async def evolucion(request: Request):
    return templates.TemplateResponse("evolucion.html", {"request": request})

@app.get("/receta", response_class=HTMLResponse)
async def receta(request: Request):
    return templates.TemplateResponse("receta.html", {"request": request})

@app.get("/indicaciones", response_class=HTMLResponse)
async def indicaciones(request: Request):
    return templates.TemplateResponse("indicaciones.html", {"request": request})

@app.get("/turnos", response_class=HTMLResponse)
async def turnos(request: Request):
    return templates.TemplateResponse("turnos.html", {"request": request})

@app.get("/registro", response_class=HTMLResponse)
async def registro_pacientes(request: Request):
    return templates.TemplateResponse("registro.html", {"request": request})
