import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'total_sqft':1250, 'bath':2, 'bhk':3})

print(r.json())