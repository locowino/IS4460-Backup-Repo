from django.contrib import admin
from movie.models import Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    pass # Empty admin class for now
admin.site.register(Movie)


#works