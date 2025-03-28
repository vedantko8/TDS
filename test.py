import requests

url = "http://127.0.0.1:8000/api/"

# Correct way to send Form data
data = {"question": "What is the capital of India?"}

response = requests.post(url, data=data)  # Use `data=` instead of `json=`

print("Response:", response.json())
