class InventoryUseCases:
    def __init__(self, db_adapter):
        self.db_adapter = db_adapter

    async def get_all_inventory(self):
        return await self.db_adapter.get_all_inventory()

    async def update_inventory(self, product_id, stock_change):
        return await self.db_adapter.update_inventory(product_id, stock_change)

    async def decrease_stock(self, product_id, quantity):
        return await self.db_adapter.decrease_stock(product_id, quantity)
