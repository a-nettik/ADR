import requests

url = 'http://127.0.0.1:5000/api/v1.0/predict'
params = {'a': 'j', 'b': 2}

response = requests.get(url, params=params)

print(response.json())  # Wyświetli odpowiedź JSON z API
