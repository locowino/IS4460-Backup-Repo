from django.db import models

# Create your models here.

class Customer(models.Model):
    name= models.CharField(max_length=50)
class Order(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    address = models.TextField()
    payment_method = models.CharField(max_length =50)