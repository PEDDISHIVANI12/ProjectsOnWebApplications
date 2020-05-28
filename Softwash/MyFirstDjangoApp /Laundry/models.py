from django.db import models

# Create your models here.
class Laundry(models.Model):
    pickup_date = models.CharField(max_length=200)
    delivery_date = models.CharField(max_length=200)
    pickup_flat = models.CharField(max_length=200)
    pickup_locality = models.CharField(max_length=200)
    pickup_pincode = models.CharField(max_length=200)
    delivery_flat = models.TextField(max_length=500)
    delivery_locality = models.TextField(max_length=500)
    delivery_pincode = models.TextField(max_length=500)
    email = models.TextField(max_length=500)
    pay = models.CharField(max_length=200)
    details = models.TextField(max_length=500)

def __str__(self):
    return self.pickup_date

class LaundryInfo_services(models.Model):
    laundry_services = models.CharField(max_length=200)

def __str__(self):
    return self.laundry_services

class Cartvalue(models.Model):
    amount = models.CharField(max_length=200)
    
    
def __str__(self):
    return self.amount
 