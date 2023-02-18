import requests
import json

response = requests.get("https://cve.circl.lu/api/browse/apache")

print(response.status_code)
print(response.text)

res = json.loads(response.text)

print(res)
