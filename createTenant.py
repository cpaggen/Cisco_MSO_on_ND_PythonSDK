import json
import sys
import mso
import urllib3
import json
import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
try:
    from credentials import MSO_IP, MSO_ADMIN, MSO_PASSWORD
except ImportError:
    sys.exit("Error: please verify credentials file format.")

tenantId = []
tenantJson = '''
{"displayName":"%s",
 "name":"%s",
 "description":"%s",
 "siteAssociations":[
   {"siteId":"6081c2155fb41db238e1c69a",
    "securityDomains":[]
   }],
 "userAssociations":[]}
'''

rc = mso.RestClient(MSO_IP, MSO_ADMIN, MSO_PASSWORD, api_version="v1")

for i in range(100):
    tenant = tenantJson % ("DemoB-"+str(i),"demoB-"+str(i),"API test "+str(i))
    resp = rc.post('/tenants', json_body=json.loads(tenant))
    allNodes = json.loads(resp.text)
    pprint.pprint(allNodes)
    tenantId.append(allNodes['id'])
    
print("Check the UI. I will now delete all tenants")
temp = raw_input("continue? ")

for i in range(len(tenantId)):
    delUrl = '/tenants/' + tenantId[i]
    resp = rc.delete(delUrl)
    print("deleted {}".format(i))
