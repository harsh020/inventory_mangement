from rest_framework import serializers

from inventory.item.models import Item, Category
from inventory.warehouse.api.v1.serializers import WarehouseSerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('is_deleted', 'created', 'modified',)


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


class ItemDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    warehouse = WarehouseSerializer()

    class Meta:
        model = Item
        fields = '__all__'


