import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
CORREO_MORSOL = os.getenv("CORREO_MORSOL")
PASSWORD_APP = os.getenv("PASSWORD_APP")

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
    # Armamos el mensaje
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"🔴 NUEVA COTIZACIÓN: {datos.servicio} - {datos.nombre}"
    msg["From"] = CORREO_MORSOL
    msg["To"] = CORREO_MORSOL
    # Esto es clave: Si le das "Responder" al correo, le contestará directamente al cliente
    msg["Reply-To"] = datos.correo 

    # Plantilla HTML para que el correo te llegue con un formato muy profesional
    html = f"""
    <html>
      <body style="font-family: Arial, sans-serif; color: #1e293b; background-color: #f8fafc; padding: 20px;">
        <div style="max-w: 600px; background: white; padding: 30px; border-radius: 8px; border-top: 5px solid #f97316; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h2 style="color: #f97316; margin-top: 0; text-transform: uppercase;">Nueva Solicitud Web - MORSOL</h2>
            <p>Has recibido una nueva solicitud de cotización desde la Landing Page.</p>
            <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 20px 0;">
            <p><strong>👤 Cliente:</strong> {datos.nombre}</p>
            <p><strong>✉️ Correo:</strong> {datos.correo}</p>
            <p><strong>📞 Teléfono:</strong> {datos.telefono}</p>
            <p><strong>⚙️ Servicio solicitado:</strong> {datos.servicio}</p>
            <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 20px 0;">
            <h3 style="color: #334155; margin-bottom: 10px;">Detalles del Proyecto:</h3>
            <div style="background-color: #f1f5f9; padding: 15px; border-radius: 5px; white-space: pre-wrap;">{datos.mensaje}</div>
            <p style="margin-top: 30px; font-size: 12px; color: #94a3b8; text-align: center;">Generado automáticamente por el servidor de Industrias Morsol</p>
        </div>
      </body>
    </html>
    """
    msg.attach(MIMEText(html, "html"))

    try:
        # Conexión al servidor seguro de Google
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(CORREO_MORSOL, PASSWORD_APP)
        # Enviar el correo
        server.sendmail(CORREO_MORSOL, CORREO_MORSOL, msg.as_string())
        server.quit()
        
        return {"status": "success", "message": "Cotización enviada exitosamente"}
    except Exception as e:
        print(f"Error al enviar correo: {e}")
        return {"status": "error", "message": "Hubo un problema enviando el correo"}