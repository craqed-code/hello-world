import requests

url = "http://192.168.10.1/api/node/mo/uni/tn-testtenant.json"

cookie = {"APIC-cookie": "z6v8vTCHwk4glgz9n4ERT4iADmNZkpFI0fCfOruDwB+0gV9eMR8W9fBhWLUxFMwN/Ub7yWkD8uRY80BcbnLiEws4U2IGcMgmI1+R7vytRH9WZRQvwRdSTgnTmmdZNPjKLM1qtUkWjcVixdYi9Jf/S1ky0XLRMyJOr4JnvJARK6w="}
payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-testtenant\",\r\n\t\t\t\"name\": \"testtenant\",\r\n\t\t\t\"rn\": \"tn-testtenant\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)
