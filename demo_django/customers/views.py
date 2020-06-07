from django.shortcuts import render, redirect
from .models import Customers
from .forms import CustomerForm

# Create your views here.

def customer_list(request):
    customers = Customers.objects.all()
    return render(request, 'customers.html',  {"customers": customers})

def customer_new(request):
    form = CustomerForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, 'customer_form.html', {'form': form})