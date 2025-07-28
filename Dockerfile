# Use official Python 3.12 slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install PyMuPDF
RUN pip install --no-cache-dir PyMuPDF

# Copy all files into the container
COPY . /app

# Default command
CMD ["python", "main.py"]