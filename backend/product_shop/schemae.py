from datetime import datetime
from typing import List
from pydantic import BaseModel
from ninja import Schema


class CategorySchema(Schema):

    name: str


class ProductSchemaBase(Schema):

    name: str
    sku: str
    category_id: int = None
    unit_price: float


class ProductSchemaIn(ProductSchemaBase):
    pass


class ProductSchemaOut(ProductSchemaBase):

    id: int


class LineModelSchema(Schema):

    product_id: int
    quantity: int


class OrderSchemaIn(Schema):
    order_items: List[LineModelSchema]


class OrderSchemaOut(Schema):
    created: datetime
    paid: bool
    total: float


class OrderSchema(Schema):
    pass
