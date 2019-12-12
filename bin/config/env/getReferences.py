import helper
import constants

# https://api.enterprise.apigee.com/v1/organizations/yemhuynh-eval/environments/prod/references
for e in constants.ENVS:
    references=[]
    relurl="environments/"+e+"/references"
    refs =helper.get(relurl)
    for r in refs:
        ref = helper.get(relurl+"/"+r)
        references.append(ref)

    helper.dumpConfig("env/"+e+"/references.json", references)