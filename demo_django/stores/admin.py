from django.contrib import admin
from .models import PaymentMethod, Store, Product, Sale, SaleDetail
# Register your models here.

admin.site.register(Store)
admin.site.register(PaymentMethod)
admin.site.register(Product)
admin.site.register(SaleDetail)

class SaleDateilInLine(admin.TabularInline):
    list_display = ['name', 'price']
    model = SaleDetail
    extra = 0

class SaleAdmin(admin.ModelAdmin):
    inlines = [SaleDateilInLine]

admin.site.register(Sale, SaleAdmin)
