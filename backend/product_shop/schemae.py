from datetime import datetime
from typing import List

from pydantic import BaseModel
from ninja import Schema


class ProductSchemaBase(Schema):

    name: str
    sku: str
    category_id: int = None
    unit_price: float


class ProductSchemaIn(ProductSchemaBase):
    pass


class ProductSchemaOut(ProductSchemaBase):

    id: int


