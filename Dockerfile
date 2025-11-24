# Use Python 3.12 base image
FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "src/main.py"]
