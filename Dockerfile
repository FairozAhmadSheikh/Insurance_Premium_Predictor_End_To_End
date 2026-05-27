# Base Image
FROM python:3.11-slim

# Workdir
WORKDIR /app

# COPY and RUN
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]