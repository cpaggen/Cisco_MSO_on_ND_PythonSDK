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

rc = mso.RestClient(MSO_IP, MSO_ADMIN, MSO_PASSWORD, api_version="v1")

postData = '''
{
    "id": "613927591f0000080a98c007",
    "displayName": "testSchema",
    "description": "",
    "templates": [
        {
            "name": "testTemplate",
            "displayName": "testTemplate",
            "tenantId": "6138f3ef1f0000520398bf81",
            "anps": [
                {
                    "name": "ap1",
                    "displayName": "ap1",
                    "anpRef": "/schemas/613927591f0000080a98c007/templates/testTemplate/anps/ap1",
                    "epgs": [
                        {
                            "name": "epg1",
                            "displayName": "epg1",
                            "epgRef": "/schemas/613927591f0000080a98c007/templates/testTemplate/anps/ap1/epgs/epg1",
                            "contractRelationships": [],
                            "subnets": [],
                            "uSegEpg": false,
                            "uSegAttrs": [],
                            "intraEpg": "unenforced",
                            "prio": "unspecified",
                            "proxyArp": false,
                            "mCastSource": false,
                            "preferredGroup": false,
                            "bdRef": "/schemas/613927591f0000080a98c007/templates/testTemplate/bds/bd1",
                            "vrfRef": "",
                            "selectors": [],
                            "epgType": "application"
                        }
                    ]
                }
            ],
            "vrfs": [
                {
                    "name": "vrf1",
                    "displayName": "vrf1",
                    "vrfRef": "/schemas/613927591f0000080a98c007/templates/testTemplate/vrfs/vrf1",
                    "l3MCast": false,
                    "preferredGroup": false,
                    "vzAnyEnabled": false,
                    "vzAnyProviderContracts": [],
                    "vzAnyConsumerContracts": [],
                    "rpConfigs": [],
                    "pcEnfPref": "enforced",
                    "ipDataPlaneLearning": "enabled",
                    "vrfDescr": ""
                }
            ],
            "bds": [
                {
                    "name": "bd1",
                    "displayName": "bd1",
                    "bdRef": "/schemas/613927591f0000080a98c007/templates/testTemplate/bds/bd1",
                    "l2UnknownUnicast": "proxy",
                    "intersiteBumTrafficAllow": false,
                    "optimizeWanBandwidth": false,
                    "l2Stretch": false,
                    "l3MCast": false,
                    "subnets": [],
                    "vrfRef": "/schemas/613927591f0000080a98c007/templates/testTemplate/vrfs/vrf1",
                    "unkMcastAct": "flood",
                    "v6unkMcastAct": "flood",
                    "arpFlood": true,
                    "multiDstPktAct": "bd-flood",
                    "dhcpLabels": [],
                    "unicastRouting": true
                }
            ],
            "contracts": [],
            "filters": [],
            "externalEpgs": [],
            "serviceGraphs": [],
            "intersiteL3outs": [],
            "templateType": "stretched-template",
            "templateSubType": [],
            "networks": [],
            "version": 2
        }
    ]
}
'''

siteData = '''
{
    "id": "613927591f0000080a98c007",
    "displayName": "testSchema",
    "description": "",
    "templates": [
        {
            "name": "testTemplate",
            "displayName": "testTemplate",
            "tenantId": "6138f3ef1f0000520398bf81",
            "anps": [
                {
                    "name": "ap1",
                    "displayName": "ap1",
                    "anpRef": "/schemas/613927591f0000080a98c007/templates/testTemplate/anps/ap1",
                    "epgs": [
                        {
                            "name": "epg1",
                            "displayName": "epg1",
                            "epgRef": "/schemas/613927591f0000080a98c007/templates/testTemplate/anps/ap1/epgs/epg1",
                            "contractRelationships": [],
                            "subnets": [],
                            "uSegEpg": false,
                            "uSegAttrs": [],
                            "intraEpg": "unenforced",
                            "prio": "unspecified",
                            "proxyArp": false,
                            "mCastSource": false,
                            "preferredGroup": false,
                            "bdRef": "/schemas/613927591f0000080a98c007/templates/testTemplate/bds/bd1",
                            "vrfRef": "",
                            "selectors": [],
                            "epgType": "application"
                        }
                    ]
                }
            ],
            "vrfs": [
                {
                    "name": "vrf1",
                    "displayName": "vrf1",
                    "vrfRef": "/schemas/613927591f0000080a98c007/templates/testTemplate/vrfs/vrf1",
                    "l3MCast": false,
                    "preferredGroup": false,
                    "vzAnyEnabled": false,
                    "vzAnyProviderContracts": [],
                    "vzAnyConsumerContracts": [],
                    "rpConfigs": [],
                    "pcEnfPref": "enforced",
                    "ipDataPlaneLearning": "enabled",
                    "vrfDescr": ""
                }
            ],
            "bds": [
                {
                    "name": "bd1",
                    "displayName": "bd1",
                    "bdRef": "/schemas/613927591f0000080a98c007/templates/testTemplate/bds/bd1",
                    "l2UnknownUnicast": "proxy",
                    "intersiteBumTrafficAllow": false,
                    "optimizeWanBandwidth": false,
                    "l2Stretch": false,
                    "l3MCast": false,
                    "subnets": [],
                    "vrfRef": "/schemas/613927591f0000080a98c007/templates/testTemplate/vrfs/vrf1",
                    "unkMcastAct": "flood",
                    "v6unkMcastAct": "flood",
                    "arpFlood": true,
                    "multiDstPktAct": "bd-flood",
                    "dhcpLabels": [],
                    "unicastRouting": true
                }
            ],
            "contracts": [],
            "filters": [],
            "externalEpgs": [],
            "serviceGraphs": [],
            "intersiteL3outs": [],
            "templateType": "stretched-template",
            "templateSubType": [],
            "networks": [],
            "version": 2
        }
    ],
    "sites": [
        {
            "siteId": "6138cf80ca038ce79fe968e6",
            "templateName": "testTemplate",
            "anps": [
                {
                    "anpRef": "/schemas/613927591f0000080a98c007/templates/testTemplate/anps/ap1",
                    "epgs": [
                        {
                            "epgRef": "/schemas/613927591f0000080a98c007/templates/testTemplate/anps/ap1/epgs/epg1",
                            "domainAssociations": [],
                            "staticPorts": [],
                            "staticLeafs": [],
                            "uSegAttrs": [],
                            "subnets": [],
                            "selectors": []
                        }
                    ]
                }
            ],
            "vrfs": [],
            "bds": [],
            "contracts": [],
            "externalEpgs": [],
            "serviceGraphs": [],
            "intersiteL3outs": [],
            "networks": []
        }
    ]
}
'''

print("Pushing blob")
resp = rc.post('/schemas', json_body=json.loads(postData))
print("Associate to site")
resp = rc.put('/schemas/613927591f0000080a98c007', json_body=json.loads(siteData))
print("Deploy to site")
resp = rc.get('/execute/schema/613927591f0000080a98c007/template/testTemplate')
print(resp.text)
