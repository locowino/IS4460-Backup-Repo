# db_populate.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_app_project.settings')
django.setup()
from movie_app_project.models import Movie
from movie_app_project.models import User

# Empty all existing rows
for movie in Movie.objects.all():
    movie.delete()

for user in User.objects.all():
    user.delete()


# Add 10 movie rows
movies_data = [
    Movie(title="Movie 1", description="Description 1", director="Director 1", release_year = (2024), budget="$10 million", runtime="120 minutes", rating=7.5, genre="Action"),
    Movie(title="Movie 2", description="Description 2", director="Director 2", release_year = (2020), budget="$20 million", runtime="110 minutes", rating=8.0, genre="Comedy"),
    Movie(title="Movie 3", description="Description 3", director="Director 3", release_year = (2021), budget="$30 million", runtime="130 minutes", rating=7.2, genre="Drama"),
    Movie(title="Movie 4", description="Description 4", director="Director 4", release_year = (2022), budget="$40 million", runtime="125 minutes", rating=7.8, genre="Action"),
    Movie(title="Movie 5", description="Description 5", director="Director 5", release_year = (2026), budget="$50 million", runtime="115 minutes", rating=8.5, genre="Comedy"),
    Movie(title="Movie 6", description="Description 6", director="Director 6", release_year = (2019), budget="$60 million", runtime="135 minutes", rating=7.6, genre="Drama"),
    Movie(title="Movie 7", description="Description 7", director="Director 7", release_year = (2018), budget="$70 million", runtime="140 minutes", rating=7.3, genre="Action"),
    Movie(title="Movie 8", description="Description 8", director="Director 8", release_year = (2017), budget="$80 million", runtime="110 minutes", rating=8.2, genre="Comedy"),
    Movie(title="Movie 9", description="Description 9", director="Director 9", release_year = (2016), budget="$90 million", runtime="125 minutes", rating=7.4, genre="Drama"),
    Movie(title="Movie 10", description="Description 10", director="Director 10", release_year = (2002), budget="$100 million", runtime="130 minutes", rating=7.7, genre="Action"),
    # Add more movies here
]

for movie in movies_data:
    movie.save()

# Add 3 user rows
users_data = [
    User(username="User1", password="password1", first_name="Ashley", last_name="Rock", email="user1@example.com"),
    User(username="User2", password="password2", first_name="Bob", last_name="Dabb", email="user2@example.com"),
    User(username="User3", password="password3", first_name="Jimmy", last_name="Johnson", email="user3@example.com")
    # Add more users here
]

for data in users_data:
    data.save()

# QuerySet statements for Movie
# Retrieve all movies
all_movies = Movie.objects.all()

# Filter for movies starting with some text
filtered_movies = Movie.objects.filter(title__startswith='Movie')

# Get one movie
movie = Movie.objects.get(title='Movie 4')

# Update one movie
update_movie = Movie.objects.get(title='Movie 5')
update_movie.genre = "Rom Com"
update_movie.save()

# Delete one movie
delete_movie = Movie.objects.get(title='Movie 8')
delete_movie.delete()

# Get data for user given a username
user = User.objects.get(username='User2')