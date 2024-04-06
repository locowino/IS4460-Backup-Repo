import requests
import json
#Define the API endpoint
api_url = 'http://localhost:8000/api/customers/'

#Customer data as an array of JSON objects
customer_data = {
    "name": "Customer X",
    "email": "customerx@example.com",
    "phone_number": "2082491492"
}

#Create customers using a single POST request
response = requests.post(api_url, data=json.dumps(customer_data), headers={'Content-Type':'application/json'})

#Check the response status and content
if response.status_code == 201:
    print("Customers creates successfully.")
else:
    print(f"Error creating customers.")