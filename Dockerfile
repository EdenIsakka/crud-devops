# Usa una imagen base ligera de Python
FROM python:3.10-slim

# Crea un directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto a la carpeta de trabajo
COPY . .

# Expone el puerto donde correrá la app (FastAPI usa 8000 por defecto)
EXPOSE 8000

# Comando para arrancar la app con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
