from django.urls import path

from inventory.warehouse.api.v1.views import *

urlpatterns = [
    path('v1/create/',  view=WarehouseCreateView.as_view(), name='warehouse_create'),
    path('v1/<int:id>/',  view=WarehouseDetailView.as_view(), name='warehouse_fetch'),
    path('v1/list/',  view=WarehouseListView.as_view(), name='warehouse_list'),
    path('v1/<int:id>/udpate',  view=WarehouseUpdateView.as_view(), name='warehouse_update'),
    path('v1/<int:id>/delete',  view=WarehouseDeleteView.as_view(), name='warehouse_delete'),
]