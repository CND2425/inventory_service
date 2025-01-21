# Inventory Service

The Inventory Service is a REST API to manage product inventory with MongoDB and RabbitMQ integration.

## Features
- Retrieve and update inventory via REST API
- Consume order updates via RabbitMQ to decrease stock

## Prerequisites
- Docker

## Run the Service
1. Build and start the service with Docker Compose:
   ```bash
   docker-compose up --build
