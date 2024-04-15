import requests
import json

id = 8

api_url = f'http://127.0.0.1:8000/movie/create_api/{id}/'

movie_data = {
    "title" : "KDRAMA!",
    "description" : "A thrilling Korean drama set in a dystopian future where a young hero discovers his destiny in a dangerous desert.",
    "director" : "Lee Chang-dong",
    "release_year" : "2024",
    "budget" : "₩200,000,000,000",
    "runtime" : "60 minutes per episode",
    "rating" : "9.5",
    "genre" : "Sci-Fi/Fantasy",
}


response = requests.put(api_url, data=json.dumps(movie_data), headers={'Content-Type': 'application/json'})

if response.status_code==200:
    print('Movie Updated Success')
else:
    print('error updating')