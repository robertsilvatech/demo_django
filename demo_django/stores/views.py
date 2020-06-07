from django.shortcuts import render, redirect
from .models import Store, ConsolidadeSale
from .forms import StoresForm

# Create your views here.

def store_list(request):
    stores = Store.objects.all()
    return render(request, 'stores.html', {"stores": stores})

def store_new(request):
    form = StoresForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('store_list')
    return render(request, 'store_form.html', {"form": form})

def consolidade_sale(request):
    sales = ConsolidadeSale.objects.all()
    return render(request, 'consolidate_sales.html', {"sales": sales})
    