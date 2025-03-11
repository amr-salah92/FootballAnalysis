# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Mandatory system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements FIRST for layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

CMD ["gunicorn", "app:create_app()", "-b", "0.0.0.0:5000"]
