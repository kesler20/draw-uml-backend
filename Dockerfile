# Use the Python 3.9 runtime as a base image
FROM railwayapp/python:3.9

# Install Graphviz using apt-get
RUN sudo apt-get update && sudo apt-get install -y graphviz

# Upgrade pip
RUN pip install --upgrade pip

# Copy your application code into the container
COPY . /app

# Install your Python dependencies
RUN pip install -r requirements.txt

# Install your package in editable mode
RUN pip install -e .
