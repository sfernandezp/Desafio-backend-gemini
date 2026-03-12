import os
from fastapi import FastAPI, HTTPException, Depends, Header
from dotenv import load_dotenv
from google import genai
import firebase_admin
from firebase_admin import credentials, firestore, auth
from datetime import datetime

# 1. Cargar las llaves del archivo .env
load_dotenv()

app = FastAPI()

# 2. Configurar la IA (Gemini)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"), http_options={'api_version': 'v1'})

# 3. Configurar la Base de Datos (Firebase)
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Ruta de bienvenida 
@app.get("/")
def home():
    return {"mensaje": "¡Bienvenido al Backend de Samuel! El servidor está vivo."}

# 4. Función de seguridad (Verificar Token)
async def verify_token(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token faltante o inválido")
    
    token = authorization.split("Bearer ")[1]
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token 
    except Exception:
        raise HTTPException(status_code=401, detail="Token no autorizado")

# 5. Endpoint del Desafío con Seguridad
@app.post("/api/chat")
async def chat_endpoint(data: dict, user: dict = Depends(verify_token)): 
    prompt = data.get("prompt")
    if not prompt:
        raise HTTPException(status_code=400, detail="Falta el prompt")

    try:
        # Llamamos a Gemini
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        texto_ia = response.text

        # Guardamos en Firebase vinculando al usuario real
        db.collection("history").add({
            "prompt": prompt,
            "respuesta": texto_ia,
            "timestamp": datetime.now(),
            "user_id": user['uid'] # <--- Vinculamos el ID del usuario
        })

        return {"respuesta": texto_ia}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))