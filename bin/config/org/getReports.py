import helper

# https://api.enterprise.apigee.com/v1/organizations/yemhuynh-eval/reports
response = helper.get("reports")
reports=[]
for q in response["qualifier"]:
    report=helper.get("reports/"+q["name"])
    reports.append(report)

helper.dumpConfig("org/reports.json", reports)
