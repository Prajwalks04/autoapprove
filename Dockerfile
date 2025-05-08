FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot code
COPY . .

# Expose port 8080 for Koyeb
EXPOSE 8080

# Start the bot
CMD ["python", "main.py"]
