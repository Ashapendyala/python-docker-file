# Use official Python image
FROM python:3.10-slim

# Set working directory inside the image
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app code
COPY . .

# Run the app
CMD ["python", "app.py"]
