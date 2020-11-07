from django.contrib import admin

from .models import Category, Product, Order, LineItem

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


class OrderLineInline(admin.TabularInline):

    model = LineItem
    fields = ["product", "quantity"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ["title", "created", "paid", "total"]
    inlines = [OrderLineInline]
