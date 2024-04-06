import requests
import json

id = 1 # the customer id

#Define the API endpoint for a specific customer
api_url = f'http://localhost:8000/api/customers/{id}/'

customer_data =     {
        "name": "Customer XXXXXX",
        "email": "customerX@example.com",
        "phone_number": "8014651863"
    }

#Send a PUT request to update the customer
response = requests.put(api_url, data=json.dumps(customer_data), headers={'Content-Type': 'application/json'})

#Check the response status code
if response.status_code == 200:
    print("Customers updates successfully.")
else:
    print("Error updating the customer.")