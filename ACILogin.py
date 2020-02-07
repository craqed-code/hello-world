import requests

url = "http://192.168.10.1/api/aaaLogin.json"

payload = "{\r\n    \"aaaUser\": {\r\n        \"attributes\": {\r\n            \"name\" : \"admin\",\r\n            \"pwd\" : \"ciscoapic\"\r\n        }\r\n    }\r\n}"
response = requests.request("POST", url, data=payload)

print(response.text)