from django.db import models

<<<<<<< HEAD
=======

>>>>>>> ede990f (Initial commit of Django project with REST API and authentication)
class Clients(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)

<<<<<<< HEAD
=======

>>>>>>> ede990f (Initial commit of Django project with REST API and authentication)
class Orders(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='orders')
    OrderDate = models.DateField()
    DeliveryDate = models.DateField()

class GoodsTypes(models.Model):
    GoodsTypeName = models.CharField(max_length=100)
    Description = models.TextField()

class Items(models.Model):
    ItemName = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    Weight = models.DecimalField(max_digits=10, decimal_places=2)
    goodstype = models.ForeignKey(GoodsTypes, on_delete=models.CASCADE, related_name='items')

class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='order_items')
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    total_weight = models.DecimalField(max_digits=10, decimal_places=2)

class Vehicles(models.Model):
    VehicleNumber = models.CharField(max_length=20, unique=True)
    Capacity = models.IntegerField()
    Licenseplate = models.CharField(max_length=20)
    VehicleName = models.CharField(max_length=100)
    goods_type = models.ForeignKey(GoodsTypes, on_delete=models.CASCADE, related_name='vehicles')

class Drivers(models.Model):
    DriverName = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15, unique=True)
    LicenseNumber = models.CharField(max_length=40, unique=True)
    vehicle = models.OneToOneField(Vehicles, on_delete=models.CASCADE, related_name='driver')

class Routes(models.Model):
    StartLocation = models.CharField(max_length=100)
    EndLocation = models.CharField(max_length=100)
    EstimatedTime = models.IntegerField()
    Distance = models.IntegerField()

class Shipments(models.Model):
    DepartureTime = models.DateTimeField()
    ArrivalTime = models.DateTimeField()
    Status = models.IntegerField()
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='shipments')
    route = models.ForeignKey(Routes, on_delete=models.CASCADE, related_name='shipments')
    vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE, related_name='shipments')

class Warehouses(models.Model):
    WarehouseName = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Capacity = models.IntegerField()

class WarehouseReservations(models.Model):
    warehouse = models.ForeignKey(Warehouses, on_delete=models.CASCADE, related_name='reservations')
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='reservations')
    Quantity = models.IntegerField()
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='warehouse_reservations')
