FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Run tests by default
CMD ["pytest", "-v"]
