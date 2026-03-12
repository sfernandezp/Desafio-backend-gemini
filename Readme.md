# Desafío Backend - API de Chat con IA (Gemini & Firebase)

Este proyecto es una API robusta desarrollada con **FastAPI** que integra el modelo de lenguaje **Gemini 2.5 Flash** de Google y utiliza **Firebase Firestore** para la persistencia de datos. Incluye un sistema de autenticación por tokens para garantizar la seguridad de las interacciones.

## 🚀 Características

- **Generación de Contenido:** Integración con la SDK de Google Generative AI (Gemini).
- **Base de Datos NoSQL:** Almacenamiento automático de prompts, respuestas y metadatos en Firebase Firestore.
- **Seguridad:** Middleware de validación de tokens para proteger los endpoints.
- **Gestión de Historial:** Vinculación de cada interacción con el ID único del usuario.

## 🛠️ Tecnologías utilizadas

- **Lenguaje:** Python 3.9+
- **Framework:** FastAPI
- **IA:** Google Gemini 2.5 Flash
- **Cloud/DB:** Firebase (Firestore & Auth)
- **Control de Versiones:** Git & GitHub

## 📋 Requisitos previos

Para ejecutar este proyecto, necesitarás:

1. Una cuenta en Google AI Studio para obtener tu `API_KEY`.
2. Un proyecto en Firebase con una cuenta de servicio generada (`serviceAccountKey.json`).
3. Python instalado en tu sistema.

## 🔧 Instalación y Configuración

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/sfernandezp/Desafio-backend-gemini.git](https://github.com/sfernandezp/Desafio-backend-gemini.git)
   cd Desafio-backend-gemini


2. **Crea y activa un entorno virtual:**
   py -m venv venv
.\venv\Scripts\activate


3. **Instala las dependencias:**
pip install -r requirements.txt


4. **Variables de Entorno:**
GEMINI_API_KEY=tu_api_key_aqui


5. **Credenciales de Firebase:**
Coloca tu archivo serviceAccountKey.json en la carpeta raíz (este archivo está excluido por seguridad en el .gitignore).

6. **Para iniciar el servidor de desarrollo, ejecuta:**
uvicorn main:app --reload


La API estará disponible en http://127.0.0.1:8080. Puedes probar el endpoint principal en /api/chat mediante una petición POST.

## 🐳 Ejecución con Docker

Si tienes Docker instalado, puedes construir y correr la aplicación con estos comandos:

1. **Construir la imagen:**
   ```bash
   docker build -t desafio-backend .

2. **Correr el contenedor:**
docker run -p 8080:8080 --env-file .env desafio-backend

Desarrollado por Samuel Fernandez - 2026.