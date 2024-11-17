from django.contrib import admin

from .models import Clients, Orders, GoodsTypes, Items, OrderItem, Vehicles, Drivers, Routes, Shipments, Warehouses, WarehouseReservations
from .models import Clients, Orders, GoodsTypes, Items, OrderItem, Vehicles, Drivers, Routes, Shipments, Warehouses, WarehouseReservations

admin.site.register(Clients)
admin.site.register(Orders)
admin.site.register(GoodsTypes)
admin.site.register(Items)
admin.site.register(OrderItem)
admin.site.register(Vehicles)
admin.site.register(Drivers)
admin.site.register(Routes)
admin.site.register(Shipments)
admin.site.register(Warehouses)
admin.site.register(WarehouseReservations)
