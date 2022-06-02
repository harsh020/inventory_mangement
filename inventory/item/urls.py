from django.urls import path

from inventory.item.api.v1.views import *

urlpatterns = [
    path('v1/create/',  view=ItemCreateView.as_view(), name='item_create'),
    path('v1/<int:id>/',  view=ItemDetailView.as_view(), name='item_fetch'),
    path('v1/list/',  view=ItemListView.as_view(), name='item_list'),
    path('v1/<int:id>/udpate/',  view=ItemUpdateView.as_view(), name='item_update'),
    path('v1/<int:id>/delete/',  view=ItemDeleteView.as_view(), name='item_delete'),
]