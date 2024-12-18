# Generated by Django 5.1.2 on 2024-10-20 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GoodsTypeName', models.CharField(max_length=100)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartLocation', models.CharField(max_length=100)),
                ('EndLocation', models.CharField(max_length=100)),
                ('EstimatedTime', models.IntegerField()),
                ('Distance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Warehouses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WarehouseName', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=100)),
                ('Quantity', models.IntegerField()),
                ('Weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('goodstype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='myapp.goodstypes')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderDate', models.DateField()),
                ('DeliveryDate', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='myapp.clients')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.items')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='myapp.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VehicleNumber', models.CharField(max_length=20, unique=True)),
                ('Capacity', models.IntegerField()),
                ('Licenseplate', models.CharField(max_length=20)),
                ('VehicleName', models.CharField(max_length=100)),
                ('goods_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='myapp.goodstypes')),
            ],
        ),
        migrations.CreateModel(
            name='Shipments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DepartureTime', models.DateTimeField()),
                ('ArrivalTime', models.DateTimeField()),
                ('Status', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipments', to='myapp.orders')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipments', to='myapp.routes')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipments', to='myapp.vehicles')),
            ],
        ),
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DriverName', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=15, unique=True)),
                ('LicenseNumber', models.CharField(max_length=40, unique=True)),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to='myapp.vehicles')),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseReservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='myapp.items')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_reservations', to='myapp.orders')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='myapp.warehouses')),
            ],
        ),
    ]
