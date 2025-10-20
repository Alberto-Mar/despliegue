# Imagen base con Python
FROM python:3.12-slim
# Crear directorio de la app
WORKDIR /app
# Copiar requisitos e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copiar el código de la app
COPY app.py .
# Exponer el puerto 8000
EXPOSE 8000
# Comando de arranque con Gunicorn
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "app:app"]
