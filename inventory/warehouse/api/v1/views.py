from rest_framework import status, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from inventory.core.models import Address
from inventory.warehouse.api.v1.serializers import WarehouseSerializer, WarehouseDetailSerializer
from inventory.warehouse.models import Warehouse


class WarehouseCreateView(GenericAPIView):
    serializer_class = WarehouseSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        validate_data = serializer.validated_data

        address = None
        if validate_data.get('address', None) is not None:
            address = validate_data.pop('address')
            address, created = Address.objects.get_or_create(**address)
        warehouse = Warehouse.objects.create(**validate_data)
        warehouse.address = address
        warehouse.save()

        response = {
            'error': False,
            'data': WarehouseDetailSerializer(warehouse).data
        }
        return Response(response, status=status.HTTP_201_CREATED)


class WarehouseDetailView(GenericAPIView):
    serializer_class = WarehouseSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, id=None):
        if id is None:
            response = {
                'error': True,
                'message': 'Expected warehouse id in url params'
            }

            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            warehouse = Warehouse.objects.get(id=id)
            response = {
                'error': False,
                'data': WarehouseDetailSerializer(warehouse).data
            }

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            response = {
                'error': False,
                'message': 'Invalid warehouse id'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class WarehouseUpdateView(GenericAPIView):
    serializer_class = WarehouseSerializer
    permission_classes = [permissions.AllowAny]

    def patch(self, request, id=None):
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data
        try:
            # print(validated_data)
            if validated_data.get('address', None) is not None:
                warehouse = Warehouse.objects.get(id=id)
                address = validated_data.pop('address')
                Address.objects.filter(id=warehouse.address.id).update(**address)
                address = Address.objects.get(id=warehouse.address.id)
                warehouse.address = address
                warehouse.save()
            if len(validated_data) > 0:
                warehouse = Warehouse.objects.filter(id=id)
                warehouse.update(**validated_data)
            warehouse = Warehouse.objects.get(id=id)

            response = {
                'error': False,
                'message': 'Warehouse successfully updated',
                'data': WarehouseDetailSerializer(warehouse).data
            }

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            response = {
                'error': True,
                'message': 'Something went wrong or warehouse does not exist'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class WarehouseDeleteView(GenericAPIView):
    serializer_class = WarehouseSerializer
    permission_classes = [permissions.AllowAny]

    def delete(self, request, id=None):
        if id is None:
            response = {
                'error': True,
                'message': 'Expected warehouse id in url params'
            }

            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            warehouse = Warehouse.objects.get(id=id)
            warehouse.is_deleted = True
            warehouse.save()

            response = {
                'error': False,
                'message': 'Warehouse deleted successfully'
            }

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            response = {
                'error': False,
                'message': 'Invalid warehouse id'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class WarehouseListView(GenericAPIView):
    serializer_class = WarehouseDetailSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Warehouse.objects.all()

    def get(self, request):
        queryset = self.get_queryset()

        response = {
            'error': False,
            'data': self.get_serializer(queryset, many=True).data
        }

        return Response(response, status=status.HTTP_200_OK)