# Usa una imagen base de Python
FROM python:3.8

# Configura el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt e instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación
COPY . /app/

# Puerto en el que tu aplicación Django escuchará
EXPOSE 8000

# Comando para ejecutar tu aplicación Django
CMD ["gunicorn", "tu_proyecto.wsgi:application", "--bind", "0.0.0.0:8000"]