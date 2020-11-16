from datetime import datetime
from typing import List

from product_shop.schemae import ProductSchemaOut


from ninja import Schema



class OrderSchema(Schema):
    pass

class LineItemSchema(Schema):
    product_id: int
    quantity: int


class OrderSchemaIn(Schema):
    order_items: List[LineItemSchema]


class OrderSchemaOut(Schema):
    id: int
    created: datetime
    paid: bool
    total: float
    title: str


