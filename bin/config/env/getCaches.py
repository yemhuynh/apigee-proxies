import helper
import constants
# https://api.enterprise.apigee.com/v1/organizations/yemhuynh-eval/environments/prod/caches

for e in constants.ENVS:
    caches=[]
    cacheNames = helper.get("environments/"+e+"/caches")
    for name in cacheNames:
        cacheInfo = helper.get("environments/"+e+"/caches/"+name)
        caches.append(cacheInfo)

    helper.dumpConfig("env/"+e+"/caches.json", caches)