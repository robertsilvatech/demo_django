from django.urls import path
from .views import customer_new, customer_list

urlpatterns = [
    path('', customer_new, name='customer_new'),
    path('list', customer_list , name='customer_list')
]