from fastapi import FastAPI, Request, Form, UploadFile, File, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fpdf import FPDF
import sqlite3
import os

app = FastAPI()

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- Templates ----------------
templates = Jinja2Templates(directory="templates")

# ---------------- Ruta base ----------------
@app.get("/")
async def root():
    return {"message": "MedSys Backend funcionando correctamente"}

# ---------------- Ruta HTML Estudios Médicos ----------------
@app.get("/estudios", response_class=HTMLResponse)
async def estudios(request: Request):
    return templates.TemplateResponse("estudios.html", {"request": request})

# ---------------- Listar archivos de estudios ----------------
@app.get("/listar-estudios")
async def listar_estudios():
    try:
        carpeta = "static/estudios"
        archivos = os.listdir(carpeta)
        return {"archivos": archivos}
    except Exception as e:
        return {"error": str(e)}

# ---------------- Eliminar estudio médico ----------------
@app.post("/eliminar-estudio")
async def eliminar_estudio(nombre_archivo: str = Form(...)):
    try:
        ruta = f"static/estudios/{nombre_archivo}"
        if os.path.exists(ruta):
            os.remove(ruta)
            return {"status": "success", "message": "Archivo eliminado"}
        else:
            return {"status": "error", "message": "Archivo no encontrado"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# ---------------- Descargar estudio individual ----------------
@app.get("/descargar-estudio/{nombre_archivo}")
async def descargar_estudio(nombre_archivo: str):
    ruta = f"static/estudios/{nombre_archivo}"
    return FileResponse(ruta, media_type="application/pdf", filename=nombre_archivo)

# ---------------- Subir estudio médico con verificación ----------------
@app.post("/subir-estudio")
async def subir_estudio(archivo: UploadFile = File(...)):
    try:
        extensiones_permitidas = [".pdf", ".jpg", ".jpeg", ".png"]
        extension = os.path.splitext(archivo.filename)[1].lower()

        if extension not in extensiones_permitidas:
            raise HTTPException(status_code=400, detail="Formato de archivo no permitido")

        ruta_guardado = f"static/estudios/{archivo.filename}"
        with open(ruta_guardado, "wb") as f:
            contenido = await archivo.read()
            f.write(contenido)

        return {"status": "success", "message": "Archivo subido correctamente"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

