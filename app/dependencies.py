from motor.motor_asyncio import AsyncIOMotorClient
from app.adapters.db_adapter import MongoDBAdapter
from app.adapters.mq_adapter import RabbitMQAdapter
from app.config import Config

# MongoDB-Client
client = AsyncIOMotorClient(Config.MONGODB_URL)

# Verbindung zur gleichen Collection wie der Product-Service
db_store = client.store
products_collection = db_store.get_collection("products")

# Adapter initialisieren
inventory_db_adapter = MongoDBAdapter(products_collection)
rabbitmq_adapter = RabbitMQAdapter(Config.RABBITMQ_URL)

def get_db_adapter():
    return inventory_db_adapter

def get_mq_adapter():
    return rabbitmq_adapter
