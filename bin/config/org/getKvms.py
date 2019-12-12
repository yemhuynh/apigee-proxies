import helper

# https://api.enterprise.apigee.com/v1/organizations/yemhuynh-eval/keyvaluemaps
mapNames = helper.get("keyvaluemaps")
kvms=[]
for name in mapNames:
    kvm=helper.get("keyvaluemaps/"+name)
    kvms.append(kvm)

helper.dumpConfig("org/kvms.json", kvms)
