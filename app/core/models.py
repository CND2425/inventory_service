from pydantic import BaseModel

class InventoryModel(BaseModel):
    product_id: str
    stock: int
