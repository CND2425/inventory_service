import os

class Config:
    MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://mongodb:27017")
    RABBITMQ_URL = os.getenv("RABBITMQ_URL", "rabbitmq")
