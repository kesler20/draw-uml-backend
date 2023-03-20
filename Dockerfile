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

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install Dependencies and your package in editable mode
RUN python -m venv /opt/venv && . /opt/venv/bin/activate && pip install -r requirements.txt && pip install -e .

RUN pip install gunicorn uvicorn

CMD ["python", "-m", "gunicorn" "--workers" "3" "-k" "uvicorn.workers.UvicornWorker" "--threads" "2" "draw_uml_backend.app:app"]