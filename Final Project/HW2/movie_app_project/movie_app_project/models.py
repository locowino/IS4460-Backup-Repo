# movie_app/models.py

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=500, null=True)
    director = models.CharField(max_length=100, null=True)
    release_year = models.DateField(max_length=50, null=True)
    budget = models.CharField(max_length=50, null=True)
    genre = models.CharField(max_length=100, null=True)
    rating = models.FloatField(max_length=50, null=True)
    runtime = models.TextField(max_length=50, null=True)

class User(models.Model):
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True, null =True, blank=True)
