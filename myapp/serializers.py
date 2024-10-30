from rest_framework import serializers
from .models import Clients, Orders, GoodsTypes, Items, OrderItem, Vehicles, Drivers, Routes, Shipments, Warehouses, WarehouseReservations

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class GoodsTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsTypes
        fields = '__all__'

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = '__all__'

class DriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = '__all__'

class RoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'

class ShipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipments
        fields = '__all__'

class WarehousesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouses
        fields = '__all__'

class WarehouseReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseReservations
        fields = '__all__'
