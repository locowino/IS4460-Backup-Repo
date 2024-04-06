from django.db import models
from django import forms
import requests

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.id} - {self.name}"

#Create necessary changes (ORDER)
class Order(models.Model):
    order_number = models.IntegerField(unique=True)  
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders', db_column='customer_id')    
    item = models.CharField(max_length=255)  
    quantity = models.IntegerField() 

    

