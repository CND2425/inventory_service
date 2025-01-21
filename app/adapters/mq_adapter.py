import aio_pika
import json
import logging
import asyncio

logging.basicConfig(level=logging.INFO)


class RabbitMQAdapter:
    def __init__(self, rabbitmq_url):
        self.rabbitmq_url = rabbitmq_url
        logging.info(f"RabbitMQ URL: {rabbitmq_url}")  # URL beim Start ausgeben

    async def connect(self):
        """
        Baut eine Verbindung zu RabbitMQ mit Retry-Logik auf.
        """
        for attempt in range(5):  # Bis zu 5 Versuche
            try:
                logging.info(f"Versuche Verbindung zu RabbitMQ: {self.rabbitmq_url}")
                connection = await aio_pika.connect_robust(self.rabbitmq_url)
                logging.info("Erfolgreich verbunden mit RabbitMQ!")
                return connection
            except Exception as e:
                logging.error(f"Verbindung fehlgeschlagen (Versuch {attempt + 1}): {e}")
                if attempt < 4:  # Warte und versuche erneut
                    await asyncio.sleep(5)  # 5 Sekunden warten
                else:
                    raise e

    async def consume_order_updates(self, db_adapter):
        """
        Konsumiert Nachrichten aus der 'order_updates'-Warteschlange und verarbeitet sie.
        """
        try:
            # Verbindung zu RabbitMQ aufbauen
            connection = await self.connect()
            channel = await connection.channel()
            await channel.set_qos(prefetch_count=1)

            # Warteschlange deklarieren
            queue = await channel.declare_queue("order_updates", durable=True)
            logging.info("Waiting for messages in 'order_updates' queue...")

            # Nachrichten konsumieren
            async for message in queue:
                async with message.process():
                    try:
                        body = json.loads(message.body)
                        product_id = body["product_id"]
                        quantity = body["quantity"]

                        logging.info(f"Received message: {body}")

                        # Lagerbestand aktualisieren
                        result = await db_adapter.decrease_stock(product_id, quantity)
                        logging.info(f"Stock updated: {result}")
                    except ValueError as e:
                        logging.error(f"Error processing message: {e}")
                    except Exception as e:
                        logging.error(f"Unexpected error: {e}")
        except Exception as e:
            logging.error(f"Failed to connect to RabbitMQ: {e}")
