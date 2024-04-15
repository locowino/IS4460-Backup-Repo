import requests
id = 9

api_url = f'http://127.0.0.1:8000/movie/create_api/{id}/'

response = requests.delete(api_url)

if response.status_code == 204:
    print('Movie Successfully Deleted')
else:
    print('Error deleting customer')
    