FROM python:3.12-slim
# WORKDIR /app
# RUN pip install flask
# RUN pip install gunicorn
# # COPY . .
# COPY requirements.txt /tmp/requirements.txt
# RUN pip install --no-cache-dir -r /tmp/requirements.txt
# COPY . .
# CMD [ "gunicorn", "--workers=5", "--bind", "0.0.0.0:8000","app:app"]

# # onather test
# FROM python:3.13-slim
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# # RUN pip install waitress
# COPY . /app
# ENV FLASK_APP=app/app.py
# CMD [ "gunicorn", "--workers=5", "--bind", "0.0.0.0:8000","app:app"]

# test code
# FROM python:3.12-slim
# WORKDIR /app
# RUN pip install flask
# # RUN pip install gunicorn
# COPY . .
# # COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# CMD [ "python","app.py"]


# new codes
# Use stable Python version (3.12 is recommended)
# FROM python:3.12-slim
# # Set work directory
# WORKDIR /app
# # Install production dependencies efficiently
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# # Copy all project files
# COPY . .
# # Expose Flask port
# EXPOSE 8000
# # Start app with Gunicorn
# CMD ["gunicorn", "--workers=5", "--bind", "0.0.0.0:8000", "app:app"]