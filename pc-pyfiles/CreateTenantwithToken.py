import requests
import json

url = "http://192.168.10.1/api/aaaLogin.json"

payload = "{\r\n    \"aaaUser\": {\r\n        \"attributes\": {\r\n            \"name\" : \"admin\",\r\n            \"pwd\" : \"ciscoapic\"\r\n        }\r\n    }\r\n}"
headers = {'Authorization': 'Basic YWRtaW46Y2lzY29hcGlj'}

response = requests.request("POST", url, data=payload, headers=headers)

#print(response.text)

json_response = json.loads(response.text)

#print response.text
#print(json_response['imdata'][0]['aaaLogin']['attributes']['token'])
# "imdata":[{"aaaLogin":{"attributes":{"token":"uOixZDUnsXwvRYllpAejecb0rt8jh4lBL8NfxdCWWL0NmEOpKDlfpvTMF2IR+Ljc7A8tP4d/VP5hN2Pj9No2MTkyJeTooFzKTx6oZ6mXNzSvU19A7iDcRVnYr9zHs0CqPlw8bLpPQONV2510C52tzBLBGrQlkHvIEihV+N39mUc="
tokenfromlogin = (json_response['imdata'][0]['aaaLogin']['attributes']['token'])

# Next API request below
url = "http://192.168.10.1/api/node/mo/uni/tn-testtenant.json"

cookie = {"APIC-cookie": tokenfromlogin }
payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-testtenant\",\r\n\t\t\t\"name\": \"testtenant\",\r\n\t\t\t\"rn\": \"tn-testtenant\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)
