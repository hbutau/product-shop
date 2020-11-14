from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from .models import Order, LineItem
from .schema import OrderSchemaIn, OrderSchemaOut

router = Router()


@router.post("")
def create_order(request, payload: OrderSchemaIn):
    order_data = payload.dict()
    lineitems = order_data.pop("order_items")
    print(lineitems)

    order = Order.objects.create(**order_data)

    for order_lines in lineitems:
        order.order_items.create(**order_lines)
    return {"id": order.id}

@router.get("", response=List[OrderSchemaOut])
def list_orders(request):
    qs = Order.objects.all()
    return qs

@router.get("/{order_id}", response=OrderSchemaOut)
def get_order(request, order_id: int):
    order = get_object_or_404(Order, id=order_id)
    return order

@router.put("/{order_id}")
def update_order(request, order_id: int, payload: OrderSchemaIn):
    update_data = payload.dict()
    lineitems = update_data.pop("order_items")
    wanted_items = [product.get("product_id") for product in lineitems if product.get("product_id", None)]
    LineItem.objects.filter(order=order_id).exclude(id__in=wanted_items).delete()
    for line in lineitems:
        product_id = line.pop('product_id')
        # TODO: Resolve error
        obj, created = LineItem.objects.update_or_create(product_id=product_id, order=Order.objects.get(id=order_id), defaults=line)
    return {"succes": "True"}


@router.delete("/{order_id}")
def destroy_order(request, order_id: int):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return {"success": "True"}
