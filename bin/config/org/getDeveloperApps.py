import helper

appIds = helper.get("apps")
developerApps = []
for id in appIds:
    app = helper.get("apps/"+id)
    developerApps.append(app)

helper.dumpConfig("org/developerApps.json", developerApps)
