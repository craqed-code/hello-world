import requests

url = "http://192.168.10.90/nuova"

payload = "<configConfMos\r\ncookie=\"1581091265/4fec9a84-1a49-49f0-8dc4-4d909f1942b2\"\r\ninHierarchical=\"false\">\r\n    <inConfigs>\r\n<pair key=\"org-root/org-PythonMaster\">\r\n    <orgOrg\r\n    name=\"PythonMaster\"\r\n    dn=\"org-root/org-PythonMaster\"\r\n    \r\n    status=\"created\"\r\n    \r\n    sacl=\"addchild,del,mod\">\r\n    </orgOrg>\r\n</pair>\r\n    </inConfigs>\r\n</configConfMos>"
headers = {
    'Content-Type': "text/xml",
    'Authorization': "Basic Y2lzY286Y2lzY28="
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
