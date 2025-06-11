# Use slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY . .

# Set environment variable to avoid Python buffering
ENV PYTHONUNBUFFERED=1

# Default command (adjust as needed)
CMD ["python", "-m", "pyseoa"]
