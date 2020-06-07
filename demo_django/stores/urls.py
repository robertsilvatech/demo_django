from django.urls import path
from .views import store_new, store_list, consolidade_sale

urlpatterns = [
    path('', store_new, name='store_new'),
    path('list', store_list , name='store_list'),
    path('sales/total', consolidade_sale, name='consolidade_sale')
]