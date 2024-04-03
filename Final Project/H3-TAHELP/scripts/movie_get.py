import requests

id=1
# I created movies and deleted them so ther is id 2-7 
# Check the database for further understanding
api_url = f'http://localhost:8001/movie/create_api/{id}'

response = requests.get(api_url)

if response.status_code==200:
    movie_data = response.json()
    print(movie_data)
else:
    print('Error retrieving customer')