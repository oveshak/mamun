from django.db import models

# Create your models here.
from django.db import models

class Checkout(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_names = models.TextField()  # Field to store product names
    product_quantities = models.JSONField(default=dict)  # New field to store product quantities as a dictionary

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.total_price} TAKA"
