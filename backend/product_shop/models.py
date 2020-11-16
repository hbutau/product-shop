from django.db import models

from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    sku = models.CharField(max_length=100, blank=False, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_products"
    )
    unit_price = models.FloatField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
