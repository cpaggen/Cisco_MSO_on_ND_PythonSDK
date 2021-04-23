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

tenantJson = '''
{"displayName":"abc","name":"abc","description":"fred","siteAssociations":[{"siteId":"6081c2155fb41db238e1c69a","securityDomains":[]}],"userAssociations":[]}
'''

rc = mso.RestClient(MSO_IP, MSO_ADMIN, MSO_PASSWORD, api_version="v1")

resp = rc.post('/tenants', json_body=json.loads(tenantJson))
allNodes = json.loads(resp.text)
pprint.pprint(allNodes)

