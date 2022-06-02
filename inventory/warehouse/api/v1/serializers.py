from rest_framework import serializers

from inventory.core.serializers import AddressSerializer, AddressDetailSerializer
from inventory.warehouse.models import Warehouse


class WarehouseSerializer(serializers.ModelSerializer):
    address = AddressSerializer(partial=True)

    class Meta:
        model = Warehouse
        fields = '__all__'


class WarehouseDetailSerializer(serializers.ModelSerializer):
    address = AddressDetailSerializer(partial=True)

    class Meta:
        model = Warehouse
        fields = '__all__'
