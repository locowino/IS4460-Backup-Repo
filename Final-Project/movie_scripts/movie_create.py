import requests
import json

api_url = 'http://127.0.0.1:8000/movie/create_api/'

movie_data = {
    "title" : "Love in Seoul",
    "description" : "A heartwarming romantic drama about two people from different worlds who find love in the bustling streets of Seoul.",
    "director" : "Park Chan-wook",
    "release_year" : "2024",
    "budget" : "₩150,000,000,000",
    "runtime" : "45 minutes per episode",
    "rating" : "9.0",
    "genre" : "Romance/Drama",
}

response = requests.post(url= api_url, data=json.dumps(movie_data),headers={'Content-Type':'application/json'})    

if response.status_code == 201:
    print('Customer created succesfully')
else:
    print(f'Error creating customer.')
    