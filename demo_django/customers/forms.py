from django import forms
from django.forms import ModelForm
from .models import Customers

class CustomerForm(ModelForm):
    class Meta:
        model = Customers
        fields = ['first_name','last_name','email', 'status']