# myapp/forms.py
from django import forms
from .models import Clients, Orders


class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'email', 'phone']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['OrderDate', 'DeliveryDate']
