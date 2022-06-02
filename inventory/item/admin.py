from django.contrib import admin

from inventory.item.models import Item
from inventory.item.models import Category


@admin.register(Category)
class ItemAdmin(admin.ModelAdmin):
    model = Category


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    model = Item
