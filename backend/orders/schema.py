from datetime import datetime
from typing import List

from product_shop.schemae import ProductSchemaOut


from ninja import Schema


class OrderSchemaOut(Schema):
    created: datetime
    paid: bool
    total: float
    title: str


class OrderSchema(Schema):
    pass

class LineItemSchema(Schema):
    product_id: int
    quantity: int


class OrderSchemaIn(Schema):
    order_items: List[LineItemSchema]



