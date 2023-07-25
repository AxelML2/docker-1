import requests

response = requests.get("http://localhost:8000/test")
print(response.text)