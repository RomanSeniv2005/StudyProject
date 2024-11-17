from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClientsViewSet, OrdersViewSet, GoodsTypesViewSet, ItemsViewSet,
    OrderItemViewSet, VehiclesViewSet, DriversViewSet, RoutesViewSet,
    ShipmentsViewSet, WarehousesViewSet, WarehouseReservationsViewSet
)

router = DefaultRouter()
router.register(r'clients', ClientsViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'goods-types', GoodsTypesViewSet)
router.register(r'items', ItemsViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'vehicles', VehiclesViewSet)
router.register(r'drivers', DriversViewSet)
router.register(r'routes', RoutesViewSet)
router.register(r'shipments', ShipmentsViewSet)
router.register(r'warehouses', WarehousesViewSet)
router.register(r'reservations', WarehouseReservationsViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Додаємо маршрути маршрутизатора
]
