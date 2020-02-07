import requests
import json

asaurl = "https://192.168.10.100/api/objects/networkobjects"

asapayload = "{\r\n  \"host\": {\r\n    \"kind\": \"IPv4Address\",\r\n    \"value\": \"100.1.1.1\"\r\n  },\r\n  \"kind\": \"object#NetworkObj\",\r\n  \"name\": \"Development\",\r\n  \"objectId\": \"Development\"\r\n}"
asaheaders = {
    'Content-Type': "application/json",
    'Authorization': "Basic ZW5hYmxlXzE6Y2lzY28="
    }

asaresponse = requests.request("POST", asaurl, verify=False, data=asapayload, headers=asaheaders)

print(asaresponse.text)

nxurl='https://192.168.10.60/ins'
switchuser='admin'
switchpassword='Passw0rd1'

myheaders={'content-type':'application/json'}
nxpayload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ;vlan 600 ;name Construction ; vlan 700 ;name Analysis ;",
    "output_format": "json"
  }
}
nxresponse = requests.post(nxurl, verify=False, data=json.dumps(nxpayload), headers=myheaders,auth=(switchuser,switchpassword)).json()


xeurl = 'http://192.168.10.80/restconf/api/config/native/ip/route'
xeheaders = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic YWRtaW46Y2lzY28="
    }
#xepayload="{    "ned:route": {        "ip-route-interface-forwarding-list": [            {                "prefix": "216.48.1.0",                "mask": "255.255.255.0",                "fwd-list": [                    {                       "fwd": "192.168.1.1"                    }                ]            }        ]    }}"
xepayload = "{\r\n\t\"ned:route\": {\r\n\t\t\"ip-route-interface-forwarding-list\": [{\r\n\t\t\t\"prefix\": \"216.48.1.0\",\r\n\t\t\t\"mask\": \"255.255.255.0\",\r\n\t\t\t\"fwd-list\": [{\r\n\t\t\t\t\"fwd\": \"10.1.1.1\"\r\n\t\t\t}]\r\n\t\t}]\r\n\t}\r\n}"

xeresponse =  requests.request("PATCH", xeurl, data=xepayload, headers=xeheaders)
print(xeresponse.text)
