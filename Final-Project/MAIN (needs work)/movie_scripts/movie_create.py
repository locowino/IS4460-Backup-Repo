import requests
import json

api_url = 'http://127.0.0.1:8000/movie/create_api/'

movie_data = {
    "title" : "Star Wars",
    "description" : "A movie about something",
    "director" : "George",
    "release_year" : "1977",
    "budget" : "$11,000,000",
    "runtime" : "120 minutes",
    "rating" : "9",
    "genre" : "Fantasy",
}

response = requests.post(url= api_url, data=json.dumps(movie_data),headers={'Content-Type':'application/json'})    

if response.status_code == 201:
    print('Customer created succesfully')
else:
    print(f'Error creating customer.')
    