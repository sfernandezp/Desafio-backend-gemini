# 1. Usamos una imagen oficial de Python como base
FROM python:3.9-slim

# 2. Establecemos la carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiamos el archivo de dependencias
COPY requirements.txt .

# 4. Instalamos las librerías necesarias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos el código fuente
COPY . .

# 6. Exponemos el puerto 8080
EXPOSE 8080

# 7. Comando para ejecutar la aplicacion
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]