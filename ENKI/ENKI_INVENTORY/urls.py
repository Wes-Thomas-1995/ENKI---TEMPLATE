from . import views
from django.urls import path

urlpatterns = [

    path('inventory/', views.inventory, name="inventory"),
    path('store-specific-inventory/<str:pk>/', views.inventory_specific, name="inventory-specific"),

    ]