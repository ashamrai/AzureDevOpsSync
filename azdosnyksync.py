from apis import snykapi

# Replace with your Snyk token
SNYK_TOKEN = ""

sonar = snykapi.SnykAPI(SNYK_TOKEN)
org_key = ""
project_key = ""

issues_json = sonar.get_issues(org_key, project_key)

#issues_json = sonar.get_orgs()

print(issues_json)

