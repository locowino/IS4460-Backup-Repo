import requests
import json

id = 8

api_url = f'http://127.0.0.1:8000/movie/create_api/{id}/'

movie_data = {
    "title" : "Dune",
    "description" : "A movie about something",
    "director" : "Denis",
    "release_year" : "2024",
    "budget" : "$190,000,000",
    "runtime" : "160 minutes",
    "rating" : "9.5",
    "genre" : "Thriller",
}

response = requests.put(api_url, data=json.dumps(movie_data), headers={'Content-Type': 'application/json'})

if response.status_code==200:
    print('Movie Updated Success')
else:
    print('error updating')