from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta():
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    sku = models.CharField(max_length=100, blank=False, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_products')
    unit_price = models.FloatField()

    def __str__(self):
        return self.product_name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)



class Order(models.Model):

    created = models.DateTimeField()
    paid = models.BooleanField(default=False)
    total = models.FloatField()


class LineItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_items")
    quantity = models.PositiveIntegerField()
