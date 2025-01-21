from fastapi import FastAPI
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware
from app.dependencies import get_db_adapter, get_mq_adapter
import asyncio

# FastAPI-App erstellen
app = FastAPI(
    title="Inventory Service",
    description="Microservice zur Lagerverwaltung mit RabbitMQ und MongoDB",
    version="1.0.0",
    docs_url='/docs',
    redoc_url='/docs',
    openapi_url='/openapi.json',
    root_path='/api/inventory',
)

# CORS-Middleware hinzufügen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8080"],  # Erlaube Anfragen von deinem Frontend
    allow_credentials=True,  # Erlaube das Setzen von Cookies
    allow_methods=["*"],  # Erlaube alle HTTP-Methoden (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Erlaube alle Header
)

# Routen registrieren
app.include_router(router)

# RabbitMQ-Consumer beim Start des Services starten
@app.on_event("startup")
async def startup_event():
    db_adapter = get_db_adapter()
    mq_adapter = get_mq_adapter()
    asyncio.create_task(mq_adapter.consume_order_updates(db_adapter))
