import helper
import constants

# https://api.enterprise.apigee.com/v1/organizations/yemhuynh-eval/environments/prod/virtualhosts

for e in constants.ENVS:
    virtualHosts=[]
    relurl = "environments/prod/virtualhosts"
    hosts = helper.get(relurl)
    for h in hosts:
        host = helper.get(relurl+"/"+h)
        virtualHosts.append(host)

    helper.dumpConfig("env/"+e+"/virtualHosts.json", virtualHosts)