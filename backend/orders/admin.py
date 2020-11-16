from django.contrib import admin

from .models import LineItem
from .models import Order


class OrderLineInline(admin.TabularInline):

    model = LineItem
    fields = ["product", "quantity"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ["title", "created", "paid", "total"]
    inlines = [OrderLineInline]
