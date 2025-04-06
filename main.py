from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Montar carpeta de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ruta: Splash inicial
@app.get("/", response_class=HTMLResponse)
async def splash():
    return FileResponse("templates/splash_screen.html")

# Ruta: Página de inicio (Menú principal)
@app.get("/index", response_class=HTMLResponse)
async def menu():
    return FileResponse("templates/index.html")

# Ruta: Registro de pacientes
@app.get("/registro", response_class=HTMLResponse)
async def registro():
    return FileResponse("templates/registro.html")

# Ruta: Historia clínica
@app.get("/historia", response_class=HTMLResponse)
async def historia():
    return FileResponse("templates/historia.html")

# Historia clínica - Formato completo
@app.get("/historia-completa", response_class=HTMLResponse)
async def historia_completa():
    return FileResponse("templates/historia-completa.html")

# Historia clínica - Formato reducido
@app.get("/historia-resumen", response_class=HTMLResponse)
async def historia_resumen():
    return FileResponse("templates/historia-resumen.html")

# Historia clínica - Evolución
@app.get("/historia-evolucion", response_class=HTMLResponse)
async def historia_evolucion():
    return FileResponse("templates/historia-evolucion.html")

# Ruta: Receta electrónica
@app.get("/receta", response_class=HTMLResponse)
async def receta():
    return FileResponse("templates/receta.html")

# Ruta: Indicaciones médicas
@app.get("/indicaciones", response_class=HTMLResponse)
async def indicaciones():
    return FileResponse("templates/indicaciones.html")

# Ruta: Turnos médicos
@app.get("/turnos", response_class=HTMLResponse)
async def turnos():
    return FileResponse("templates/turnos.html")

# Ruta: Búsqueda de pacientes
@app.get("/busqueda", response_class=HTMLResponse)
async def busqueda():
    return FileResponse("templates/busqueda.html")
