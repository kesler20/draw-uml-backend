# Use the Python 3.9 runtime as a base image
FROM python:3.9-slim-buster

# Update the package list and install graphviz
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    graphviz

# Clean up the package list to reduce the image size
RUN rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy your application code into the container
COPY . /app

# Install your Python dependencies
RUN pip install -r requirements.txt

# Install your package in editable mode
RUN pip install -e .
