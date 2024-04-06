import requests
import json

id = 1  # the order id

# Define the API endpoint for a specific order
api_url = f'http://localhost:8000/api/orders/{id}/'

order_data = {
    "order_number": "1234",  
    "customer_name": "1 - ASHLEY DABB",  
    "item": "Product Y",  
    "quantity": 3  
}

# Send a PUT request to update the order
response = requests.put(api_url, json=order_data, headers={'Content-Type': 'application/json'})

# Check the response status code
if response.status_code == 200:
    print("Order updated successfully.")
else:
    print("Error updating the order.")
