from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_page, name='welcome_page'),
    path('clients/', views.client_list, name='client_list'),
    #path('register/', views.register, name='register'),
    path('add/', views.client_add, name='client_add'),
    path('<int:client_id>/', views.client_detail, name='client_detail'),
    path('<int:client_id>/edit/', views.client_edit, name='client_edit'),
    path('<int:client_id>/delete/', views.client_delete, name='client_delete'),
    path('orders/create/', views.create_order, name='create_order'),
    path('orders/', views.orders_list, name='orders_list'),
]
