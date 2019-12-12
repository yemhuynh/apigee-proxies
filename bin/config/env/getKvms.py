import json
import helper
import constants

# get env-specific kvms
for e in constants.ENVS:
    response=helper.get("environments/" + e + "/keyvaluemaps")
    envKvm=[]
    for kvm in response:
        response = helper.get("environments/"+e+"/keyvaluemaps/" + kvm)
        envKvm.append(response)

    # now write to file
    helper.dumpConfig("env/"+e+"/kvms.json", envKvm)


