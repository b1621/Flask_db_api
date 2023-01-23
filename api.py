import requests
import json

# response = requests.get("https://randomuser.me/api/")
# response = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:o:microsoft:windows_10:1607")
# response = requests.get("https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=microsoft")
response = requests.get("http://docs.opencve.io/api/vendors/wordpress")

print(response.status_code)
print(response.text)

# res = json.loads(response.text)

# print(res)