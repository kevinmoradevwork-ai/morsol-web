import smtplib
import os
import os
import resend
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
CORREO_MORSOL = os.getenv("CORREO_MORSOL")
PASSWORD_APP = os.getenv("PASSWORD_APP")
resend.api_key = os.environ.get("RESEND_API_KEY")

app = FastAPI(title="MORSOL API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FormularioContacto(BaseModel):
    nombre: str
    correo: str
    telefono: str
    servicio: str
    mensaje: str

# --- CONFIGURACIÓN DE CORREO ---
CORREO_MORSOL = "administracion@industriasmorsol.com"
# Pega aquí la contraseña de 16 letras sin espacios (ej: "abcd efgh ijkl mnop" -> "abcdefghijklmnop")
PASSWORD_APP = "xvpi xbdo iets mbcw" 

@app.post("/api/contacto")
async def recibir_contacto(datos: FormularioContacto):
    
    # Preparar el paquete de datos para Resend
    params = {
        "from": "onboarding@resend.dev", # Resend usa este por defecto para pruebas
        "to": ["kevinmoradevwork@gmail.com"],
        "subject": f"🔴 NUEVA COTIZACIÓN: {datos.servicio} - {datos.nombre}",
        "reply_to": datos.correo, # ¡Mantenemos tu funcionalidad de responder directo al cliente!
        "html": f"""
        <h3>Nueva solicitud de contacto</h3>
        <p><strong>Cliente:</strong> {datos.nombre}</p>
        <p><strong>Correo:</strong> {datos.correo}</p>
        <p><strong>Servicio:</strong> {datos.servicio}</p>
        <p><strong>Mensaje:</strong> {datos.mensaje}</p>
        """
    }
    
    try:
        # Enviar el correo con la API
        email = resend.Emails.send(params)
        return {"status": "success", "message": "¡Cotización enviada con éxito!"}
    except Exception as e:
        # Si algo falla, lo imprimimos en Render para saber qué pasó
        print(f"Error al enviar correo: {e}")
        return {"status": "error", "message": "Hubo un problema al enviar el mensaje"}