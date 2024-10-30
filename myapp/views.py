from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Clients, Orders, GoodsTypes, Items, OrderItem, Vehicles, Drivers, Routes, Shipments, Warehouses, WarehouseReservations
from .serializers import (
    ClientsSerializer, OrdersSerializer, GoodsTypesSerializer, ItemsSerializer,
    OrderItemSerializer, VehiclesSerializer, DriversSerializer, RoutesSerializer,
    ShipmentsSerializer, WarehousesSerializer, WarehouseReservationsSerializer
)
from .repositories.clientrepository import ClientRepository


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    repository = ClientRepository()

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class GoodsTypesViewSet(viewsets.ModelViewSet):
    queryset = GoodsTypes.objects.all()
    serializer_class = GoodsTypesSerializer

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class VehiclesViewSet(viewsets.ModelViewSet):
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer

class DriversViewSet(viewsets.ModelViewSet):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer

class RoutesViewSet(viewsets.ModelViewSet):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer

class ShipmentsViewSet(viewsets.ModelViewSet):
    queryset = Shipments.objects.all()
    serializer_class = ShipmentsSerializer

class WarehousesViewSet(viewsets.ModelViewSet):
    queryset = Warehouses.objects.all()
    serializer_class = WarehousesSerializer

class WarehouseReservationsViewSet(viewsets.ModelViewSet):
    queryset = WarehouseReservations.objects.all()
    serializer_class = WarehouseReservationsSerializer

