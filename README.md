# Inventory Service

## Beschreibung
Der **Inventory Service** ist ein Bestandteil der Microservices-Architektur einer E-Commerce-Anwendung. Er bietet eine REST-API zur Verwaltung des Lagerbestands und zur Synchronisierung von Bestellungen mit der Produktverfügbarkeit.

### Hauptfunktionen:
1. **Bestandsverwaltung**: Abrufen, Aktualisieren und Synchronisieren des Lagerbestands.
2. **Produktverfügbarkeit prüfen**: Überprüfen, ob Produkte verfügbar sind.
3. **Ereignisverarbeitung**: Synchronisierung von Bestandsänderungen durch RabbitMQ-Nachrichten.

Dieser Service wurde mit **FastAPI** entwickelt und nutzt **MongoDB** zur Speicherung von Bestandsdaten sowie **RabbitMQ** für die Nachrichtenverarbeitung.

---

## Technologien
1. **FastAPI**: Framework für die API-Entwicklung.
2. **MongoDB**: NoSQL-Datenbank zur Speicherung von Bestandsdaten.
3. **RabbitMQ**: Message-Broker für die Synchronisierung.
4. **Docker**: Containerisierung des Services.
5. **GitHub Actions**: CI/CD-Pipeline zur Qualitätssicherung.

---

## Verwendete Endpunkte
### Inventory Endpoints:
1. **GET** `/inventory/` - Listet alle Produkte mit ihrem aktuellen Lagerbestand.
2. **GET** `/inventory/{product_id}` - Ruft den Lagerbestand eines spezifischen Produkts ab.
3. **PUT** `/inventory/{product_id}` - Aktualisiert den Lagerbestand eines Produkts.
4. **POST** `/sync/` - Synchronisiert Bestandsänderungen basierend auf RabbitMQ-Ereignissen.

---

## Installation und Verwendung
### Voraussetzungen
- **Python 3.9+**
- **Docker** und **Docker Compose**

### Lokale Ausführung
- **Repository klonen**:
  ```bash
  git clone <REPOSITORY_URL>
  cd inventory_service
  ```

- **Virtuelle Umgebung erstellen und aktivieren**:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Auf Windows: venv\Scripts\activate
  ```

- **Abhängigkeiten installieren**:
  ```bash
  pip install -r requirements.txt
  ```

- **Service starten**:
  ```bash
  uvicorn app.main:app --host 0.0.0.0 --port 8005
  ```

### Docker-Ausführung
- **Docker-Image erstellen und starten**:
  ```bash
  docker build -t inventory_service .
  docker run -p 8005:8005 inventory_service
  ```

- **Alternativ mit Docker Compose** (aus dem Compose-Repository):
  ```bash
  docker-compose up -d
  ```

### API-Dokumentation
FastAPI bietet eine automatisch generierte API-Dokumentation:
- Swagger UI: [http://localhost:8005/docs](http://localhost:8005/docs)
- ReDoc: [http://localhost:8005/redoc](http://localhost:8005/redoc)

---

## Datenbank
1. **MongoDB** wird verwendet, um Bestandsdaten persistent zu speichern.
2. Standardmäßig verbindet sich der Service zu `mongodb://localhost:27017`.
3. Anpassung der URL über Umgebungsvariablen:
   ```env
   MONGODB_URL=mongodb://<host>:<port>
   ```

---

## Tests
1. **Testumgebung installieren**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Tests ausführen**:
   ```bash
   pytest tests/
   ```

---

## CI/CD
1. Der Service verwendet **GitHub Actions**, um Tests und Linting automatisch bei jedem Commit auszuführen.
2. Die Konfiguration befindet sich in `.github/workflows/ci.yml`.

---

## Umgebungsvariablen
1. `MONGODB_URL`: MongoDB-Verbindungs-URL.
2. `RABBITMQ_URL`: URL des RabbitMQ-Brokers.

---
