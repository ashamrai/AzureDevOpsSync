from apis import sorarcloudapi

# Replace with your SonarCloud token
SONARCLOUD_TOKEN = ""

sonar = sorarcloudapi.SonarAPI(SONARCLOUD_TOKEN, "")
project_key = ""

issues_responce = sorarcloudapi.IssesResponse(sonar.get_project_issues(project_key))

issues = issues_responce.get_issues()
print(issues)

