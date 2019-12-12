import helper

devEmails = helper.get("developers")

developers=[]
for email in devEmails:
    developer =helper.get("developers/"+email)
    developers.append(developer)

helper.dumpConfig("org/developers.json", developers)