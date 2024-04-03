from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=500, null=True)
    director = models.CharField(max_length=100, null=True)
    release_year = models.CharField(max_length=50, null=True)
    budget = models.CharField(max_length=50, null=True)
    runtime = models.CharField(max_length=50, null=True)
    rating = models.CharField(max_length=50, null=True)
    genre = models.CharField(max_length=50, null=True)