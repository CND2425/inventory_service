from bson import ObjectId


class MongoDBAdapter:
    def __init__(self, products_collection):
        self.products_collection = products_collection

    async def get_all_inventory(self):
        # Alle Produkte aus der Datenbank abfragen
        products = await self.products_collection.find({}, {"_id": 1, "name": 1, "stock_quantity": 1}).to_list(
            length=None)
        # ObjectId zu String umwandeln
        for product in products:
            product["_id"] = str(product["_id"])
        return products

    async def get_inventory_by_product_id(self, product_id):
        # Produkt basierend auf der ID finden
        return await self.products_collection.find_one({"_id": ObjectId(product_id)})

    async def update_inventory(self, product_id, stock_change):
        # Produktbestand aktualisieren
        product = await self.products_collection.find_one({"_id": ObjectId(product_id)})
        if not product:
            raise ValueError(f"Product with ID {product_id} does not exist.")

        new_stock = product["stock_quantity"] + stock_change
        if new_stock < 0:
            raise ValueError("Insufficient stock")

        updated_product = await self.products_collection.find_one_and_update(
            {"_id": ObjectId(product_id)},
            {"$set": {"stock_quantity": new_stock}},
            return_document=True
        )
        return {"product_id": str(product_id), "stock_quantity": updated_product["stock_quantity"]}

    async def decrease_stock(self, product_id, quantity):
        # Lagerbestand verringern
        return await self.update_inventory(product_id, -quantity)
