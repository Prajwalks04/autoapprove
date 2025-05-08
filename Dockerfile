# Use the official Python image as a base
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Set environment variables (optional, can be replaced by Koyeb environment config)
ENV PYTHONUNBUFFERED 1

# Expose port 8080 (for health checks)
EXPOSE 8080

# Command to run the application using FastAPI with Uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
