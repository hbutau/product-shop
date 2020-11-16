from ninja import Router
from typing import List

from .schemae import ProductSchemaOut
from .models import Product


router = Router()

@router.get("", response=List[ProductSchemaOut])
def get_orders(request):
    qs = Product.objects.all()
    return qs
