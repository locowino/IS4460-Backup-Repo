import requests

# Define the API endpoint for orders
api_url = 'http://localhost:8000/api/orders/'

# Order data as a dictionary
order_data = {
    "order_number": "1234",  
    "customer_name": "1 - ASHLEY DABB",  
    "item": "Product X",
    "quantity": 2
}

# Create order using a single POST request
response = requests.post(api_url, json=order_data)

# Check the response status and content
if response.status_code == 201:
    print("Order created successfully.")
else:
    print("Error creating order.")