import requests
import json

with open(r'resume-optimizer\examples\sample_request.json') as f:
    data = json.load(f)

response = requests.post('http://localhost:5000/optimize', json=data)
print(response.json())