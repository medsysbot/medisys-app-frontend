from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Montar la carpeta de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Carpeta donde están los templates HTML
templates = Jinja2Templates(directory="templates")

# Página inicial - Menú principal de navegación
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Ruta para historia clínica completa
@app.get("/historia_completa", response_class=HTMLResponse)
async def historia_completa(request: Request):
    return templates.TemplateResponse("historia_completa.html", {"request": request})

# Ruta para historia clínica resumida
@app.get("/historia_resumida", response_class=HTMLResponse)
async def historia_resumida(request: Request):
    return templates.TemplateResponse("historia_resumida.html", {"request": request})

# Ruta para evolución diaria
@app.get("/evolucion", response_class=HTMLResponse)
async def evolucion(request: Request):
    return templates.TemplateResponse("evolucion.html", {"request": request})

# Ruta para receta médica
@app.get("/receta", response_class=HTMLResponse)
async def receta(request: Request):
    return templates.TemplateResponse("receta.html", {"request": request})

# Ruta para indicaciones médicas
@app.get("/indicaciones", response_class=HTMLResponse)
async def indicaciones(request: Request):
    return templates.TemplateResponse("indicaciones.html", {"request": request})
