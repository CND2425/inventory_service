from fastapi import APIRouter, Depends
from app.dependencies import get_db_adapter
from app.core.use_cases import InventoryUseCases
from pydantic import BaseModel

router = APIRouter()


class InventoryUpdateRequest(BaseModel):
    stock_change: int


@router.get("/inventory/")
async def get_inventory(db_adapter=Depends(get_db_adapter)):
    inventory_use_cases = InventoryUseCases(db_adapter)
    return await inventory_use_cases.get_all_inventory()


@router.put("/inventory/{product_id}")
async def update_inventory(product_id: str, update: InventoryUpdateRequest, db_adapter=Depends(get_db_adapter)):
    inventory_use_cases = InventoryUseCases(db_adapter)
    return await inventory_use_cases.update_inventory(product_id, update.stock_change)

@router.get("/")
async def root():
    """
    Test-Endpunkt, um sicherzustellen, dass die API läuft.
    """
    return {"message": "Inventory Service is running"}
