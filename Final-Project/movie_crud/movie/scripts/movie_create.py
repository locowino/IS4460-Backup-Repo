import requests
import json

api_url = 'http://localhost:8000/api/movies/'

movie_data = {
    "title": "Interstellar",
    "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
    "director": "Christopher Nolan",
    "release_year": "2014",
    "budget": "165000000",
    "runtime": "169",
    "rating": "8.6",
    "genre": "Sci-Fi"
}
response = requests.post(api_url, json=movie_data)

if response.status_code == 201:
    print("Movie created successfully!")
else:
    print(f"Error creating movie!")