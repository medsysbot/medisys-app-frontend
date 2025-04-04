from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Montar carpetas estáticas y templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Pantalla principal
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Historia clínica completa
@app.get("/historia-completa", response_class=HTMLResponse)
async def historia_completa(request: Request):
    return templates.TemplateResponse("historia_completa.html", {"request": request})

# Historia clínica resumida
@app.get("/historia-resumida", response_class=HTMLResponse)
async def historia_resumida(request: Request):
    return templates.TemplateResponse("historia_resumida.html", {"request": request})

# Evolución diaria
@app.get("/evolucion-diaria", response_class=HTMLResponse)
async def evolucion_diaria(request: Request):
    return templates.TemplateResponse("evolucion_diaria.html", {"request": request})

# Receta médica
@app.get("/receta", response_class=HTMLResponse)
async def receta(request: Request):
    return templates.TemplateResponse("receta.html", {"request": request})

# Indicaciones médicas
@app.get("/indicaciones", response_class=HTMLResponse)
async def indicaciones(request: Request):
    return templates.TemplateResponse("indicaciones.html", {"request": request})
