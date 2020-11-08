from ninja import Router
from typing import List

from .schemae import OrderSchemaIn, OrderSchemaOut, ProductSchemaOut
from .models import Product, Order

router = Router()


@router.post("")
def create_order(request, payload: OrderSchemaIn):
    order_data = payload.dict()
    lineitems = order_data.pop("order_items")

    order = Order.objects.create(**order_data)

    for order_lines in lineitems:
        order.order_items.create(**order_lines)
    return {"id": order.id}


@router.get("", response=List[ProductSchemaOut])
def get_orders(request):
    qs = Product.objects.all()
    return qs
