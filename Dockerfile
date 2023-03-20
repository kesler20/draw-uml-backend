# Use the Python 3.9 runtime as a base image
FROM python:3.9-slim-buster

# Update the package list and install graphviz
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    graphviz

# Clean up the package list to reduce the image size
RUN rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install Dependencies and your package in editable mode
RUN python -m venv /opt/venv && . /opt/venv/bin/activate  

RUN /opt/venv/bin/python -m pip install --upgrade pip

RUN /opt/venv/bin/python -m pip install -r requirements.txt

RUN /opt/venv/bin/python -m pip install -e .

CMD ["/opt/venv/bin/python3", "-m", "gunicorn", "--workers", "3", "-k" ,"uvicorn.workers.UvicornWorker" ,"--threads","2" ,"draw_uml_backend.app:app"]