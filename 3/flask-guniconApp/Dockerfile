# Imagen base oficial de Python
FROM python:3.12-slim
# Crear y usar el directorio de trabajo
WORKDIR /app
# Copiar archivos de dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copiar el código fuente
COPY app/ ./app
# Exponer el puerto 8000 (Gunicorn usará este por defecto)
EXPOSE 8000
# Comando de arranque: Gunicorn ejecuta la app Flask
# "app.main:app" → módulo:ruta del objeto Flask
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.main:app"]