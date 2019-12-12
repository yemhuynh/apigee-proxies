import helper

# https://api.enterprise.apigee.com/v1/organizations/yemhuynh-eval/userroles

roles = helper.get("userroles")

userRoles=[]
for r in roles:
    if r == 'devadmin':
        continue
    permissions = helper.get("userroles/"+r+"/permissions")
    permissions["name"]=r
    userRoles.append(permissions)

helper.dumpConfig("org/userroles.json", userRoles)

