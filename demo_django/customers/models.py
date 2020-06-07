from django.db import models

# Create your models here.

class Customers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    status = models.BooleanField()
    
    def __str__(self):
        return self.first_name
