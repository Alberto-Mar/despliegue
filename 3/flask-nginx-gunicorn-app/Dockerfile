# Imagen base de Python
FROM python:3.12-slim
WORKDIR /app
# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copiar la aplicación
COPY app/ ./app
# Exponer el puerto interno (Gunicorn)
EXPOSE 8000
# Comando de arranque de Gunicorn
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "app.main:app"]