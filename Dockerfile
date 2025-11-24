FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src
COPY main.py ./main.py
COPY test.py ./test.py

EXPOSE 8000

CMD ["python", "src/main.py"]
