from django.shortcuts import render, get_object_or_404, redirect
from myapp.models import Clients, Orders
from myapp.forms import ClientForm, OrderForm

def client_list(request):
    clients = Clients.objects.all()
    return render(request, 'frontend/list.html', {'clients': clients})

def client_detail(request, client_id):
    client = get_object_or_404(Clients, id=client_id)
    return render(request, 'frontend/detail.html', {'client': client})


def client_add(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'frontend/form.html', {'form': form, 'form_title': 'Add Client'})


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
    return render(request, 'frontend/create_order.html', {
        'client_form': client_form,
        'order_form': order_form,
    })

def client_edit(request, client_id):
    client = get_object_or_404(Clients, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'frontend/form.html', {'form': form, 'form_title': 'Edit Client'})

def client_delete(request, client_id):
    client = get_object_or_404(Clients, id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'frontend/delete.html', {'client': client})

def orders_list(request):
    orders = Orders.objects.select_related('client').all()
    return render(request, 'frontend/orders_list.html', {'orders': orders})

def welcome_page(request):
    return render(request, 'frontend/welcome.html')

