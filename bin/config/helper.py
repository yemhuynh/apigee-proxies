import constants
import requests
import json
import os
import errno

def get(suffix):
    print(constants.APIGEE_MGMT_API_BASE_URL+suffix)
    response=requests.get(constants.APIGEE_MGMT_API_BASE_URL+suffix, headers={'Accept': 'application/json'}, auth=(constants.username, constants.pwd))
    assert response.status_code==200
    print(response.json())
    return response.json()

def dumpConfig(relativePath,content):
    fileDest=constants.CONFIG_ROOT+relativePath
    if not os.path.exists(os.path.dirname(fileDest)):
        try:
            os.makedirs(os.path.dirname(fileDest))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    with open(fileDest, 'w') as outfile:
        json.dump(content, outfile, indent=4, sort_keys=True)