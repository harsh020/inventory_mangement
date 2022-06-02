from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response

from inventory.item.api.v1.serializers import ItemSerializer, CategorySerializer, ItemDetailSerializer
from inventory.item.models import Item, Category
from inventory.warehouse.models import Warehouse


class ItemCreateView(GenericAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        item = Item.objects.create(**validated_data)

        response = {
            'error': False,
            'data': ItemDetailSerializer(item).data,
        }

        return Response(response, status=status.HTTP_201_CREATED)


class ItemDetailView(GenericAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, id=None):

        if id is None:
            response = {
                'error': True,
                'message': 'Expected item id in url params'
            }

            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            item = Item.objects.get(id=id)
            response = {
                'error': False,
                'data': ItemDetailSerializer(item).data
            }

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            response = {
                'error': False,
                'message': 'Invalid item id'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ItemUpdateView(GenericAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny]

    def patch(self, request, id=None):
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        if validated_data.get('warehouse', None) is not None:
            warehouse = Warehouse.objects.get(**validated_data.pop('warehouse'))
            if warehouse is not None:
                response = {
                    'error': True,
                    'message': 'Cannot update item. Update warehouse separately.'
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            Item.objects.filter(id=id).update(**validated_data)
            item = Item.objects.get(id=id)

            response = {
                'error': False,
                'message': 'Item successfully updated',
                'data': ItemDetailSerializer(item).data
            }

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            response = {
                'error': True,
                'message': 'Something went wrong or item does not exist'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ItemDeleteView(GenericAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny]

    def delete(self, request, id=None):
        if id is None:
            response = {
                'error': True,
                'message': 'Expected item id in url params'
            }

            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            item = Item.objects.get(id=id)
            item.is_deleted = True
            item.save()

            response = {
                'error': False,
                'message': 'Item deleted successfully'
            }

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            response = {
                'error': False,
                'message': 'Invalid item id'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ItemListView(GenericAPIView):
    serializer_class = ItemDetailSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Item.objects.all()

    def get(self, request):
        warehouse = request.GET.get('warehouse', None)

        queryset = self.get_queryset()
        if warehouse is not None:
            queryset = queryset.filter(warehouse_id=warehouse)
        response = {
            'error': False,
            'data': self.get_serializer(queryset, many=True).data
        }

        return Response(response, status=status.HTTP_200_OK)






