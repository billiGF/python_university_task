FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy main.py and src/ folder
COPY main.py .
COPY src/ ./src
COPY .env .env

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
