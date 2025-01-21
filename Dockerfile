FROM python:3.9-slim

# Systemabhängigkeiten installieren
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        libssl-dev && \
    rm -rf /var/lib/apt/lists/*

# Arbeitsverzeichnis festlegen
WORKDIR /app

# Pip und pip-tools installieren
RUN pip install --upgrade pip && \
    pip install pip-tools

# requirements.in kopieren und requirements.txt generieren
COPY requirements.in .
RUN pip-compile requirements.in

# Abhängigkeiten installieren
RUN pip install --no-cache-dir -r requirements.txt

# Anwendungscode kopieren
COPY . .

# PYTHONPATH setzen
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Port exponieren
EXPOSE 8005

# Startbefehl festlegen
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8005"]
