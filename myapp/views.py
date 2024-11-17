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
from django.shortcuts import render, redirect
from .forms import ClientForm, OrderForm


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

def welcome_page(request):
    return render(request, 'frontend/welcome.html')
'''
def client_add(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'frontend/form.html', {'form': form})
'''
def create_order(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        order_form = OrderForm(request.POST)
        if client_form.is_valid() and order_form.is_valid():
            client = client_form.save()
            order = order_form.save(commit=False)
            order.client = client
            order.save()
            return redirect('orders_list')
    else:
        client_form = ClientForm()
        order_form = OrderForm()
    return render(request, 'create_order.html', {
        'client_form': client_form,
        'order_form': order_form,
    })


