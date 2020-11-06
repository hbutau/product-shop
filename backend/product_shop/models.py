from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100, blank=False)
    sku = models.CharField(max_length=100, blank=False)
    # category = model.
    tags = models.ForeignKey(Tag, related_name='product_tags', on_delete=models.CASCADE)
    pass


class Category(models.Model):
    category_name = models.CharField(max_lenght=100)
           

class Tag(models.Model):
    name = models.CharField()
