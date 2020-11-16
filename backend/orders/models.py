from django.db import models

from product_shop.models import Product


class Order(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    @property
    def total(self):
        return sum([line.product.unit_price * line.quantity for line in self.order_items.all()])

    @property
    def title(self):
        return f"Order #{self.id}"

    def __str__(self):
        return self.title


class LineItem(models.Model):

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_items"
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name
