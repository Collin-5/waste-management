from django.shortcuts import redirect, render
from .models import Clients, Invoice
from .forms import ClientAddForm

# Create your views here.

def client_list(request):
    data = Clients.objects.all()
    context = {
        'clients': data
    }
    return render(request, 'clients/list.html', context)

def add_clients(request):
    form = ClientAddForm()
    if request.method == 'POST':
        form = ClientAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')
    content = {
        'form': form
    }
    return render(request, 'clients/add.html', content)