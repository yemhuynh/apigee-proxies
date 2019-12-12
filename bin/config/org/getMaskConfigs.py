import helper

# https://api.enterprise.apigee.com/v1/organizations/yemhuynh-eval/maskconfigs

configs=helper.get("maskconfigs")
maskConfigs=[]
for name in configs:
    config = helper.get("maskconfigs/"+name)
    maskConfigs.append(config)

helper.dumpConfig("org/maskconfigs.json", maskConfigs)