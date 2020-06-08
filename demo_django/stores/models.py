from django.db import models

# Create your models here.

class PaymentMethod(models.Model):
    name = models.CharField(max_length=20)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
        
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField('Preço', max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

class Sale(models.Model):
    store = models.ForeignKey(Store, null=True, blank=True, on_delete=models.PROTECT)
    payment_method = models.ForeignKey(PaymentMethod, null=True, blank=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.id)
