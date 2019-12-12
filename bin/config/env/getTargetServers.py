import helper
import constants
# https://api.enterprise.apigee.com/v1/organizations/yemhuynh-eval/environments/test/targetservers


for e in constants.ENVS:
    targetServers=[]
    relurl = "environments/"+e+"/targetservers"
    servers = helper.get(relurl)
    for name in servers:
        server = helper.get(relurl+"/"+name)
        targetServers.append(server)

    helper.dumpConfig("env/"+e+"/targetServers.json", targetServers)

