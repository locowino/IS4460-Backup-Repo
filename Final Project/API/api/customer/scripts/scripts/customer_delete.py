import requests

id = 1 # the customer id

#Define the API endpoint for a specific customer
api_url = f'http://localhost:8000/api/customers/{id}/'

#Send a DELETE request to retrieve the customer
response = requests.delete(api_url)

#Check the response status code
if response.status_code == 204:
    print("Customer deleted successfully.")
else:
    print("Error deleting the customer.")