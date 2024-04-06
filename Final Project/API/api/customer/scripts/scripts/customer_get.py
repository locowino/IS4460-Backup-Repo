import requests

id = 1 #the customer id

#Define the API endpoint for a specific customer
api_url = f'http://localhost:8000/api/customers/{id}'

#Send a GET request to retreive the customer
response = requests.get(api_url)

#Check the response status code
if response.status_code == 200:
    customer_data = response.json()
    print(customer_data)
else:
    print("Error retreiving the customer")
