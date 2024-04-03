import requests
id = 9

api_url = f'http://localhost:8001/movie/create_api/{id}/'

response = requests.delete(api_url)

if response.status_code == 204:
    print('Movie Deleted Success')
else:
    print('Error deleting customer')