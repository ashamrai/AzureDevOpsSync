import requests

class SonarAPI:
    def __init__(self, token, organization=None):
        self.token = token
        self.organization = organization
        self.base_url = "https://sonarcloud.io/api"
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def get_project(self, project_key):
        url = f"{self.base_url}/projects/search?projects={project_key}&organization={self.organization}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_project_metrics(self, project_key):
        url = f"{self.base_url}/measures/component?component={project_key}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_project_issues(self, project_key):
        url = f"{self.base_url}/issues/search?componentKeys={project_key}&organization={self.organization}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_project_activity(self, project_key):
        url = f"{self.base_url}/project_analyses/search?project={project_key}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_project_activity_metrics(self, project_key, analysis_key):
        url = f"{self.base_url}/project_analyses/search?project={project_key}&analysis={analysis_key}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_project_activity_issues(self, project_key, analysis_key):
        url = f"{self.base_url}/issues/search?componentKeys={project_key}&analysisId={analysis_key}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_project_activity_coverage(self, project_key, analysis_key):
        url = f"{self.base_url}/measures/component?component={project_key}&analysisId={analysis_key}&metricKeys=coverage"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_project_activity_duplications(self, project_key, analysis_key):
        url = f"{self.base_url}/measures/component?component={project_key}&analysisId={analysis_key}&metricKeys=duplicated_lines_density"
        response = requests.get(url, headers=self.headers)
        return response.json()

class IssesResponse:
    def __init__(self, response):
        self.response = response

    def get_issues(self):
        issues = []
        for issue in self.response["issues"]:
            issues.append({
                "key": issue["key"],
                "rule": issue["rule"],
                "severity": issue["severity"],
                "message": issue["message"],
                "line": issue["line"],
                "status": issue["status"],
                "author": issue["author"],
            })
        return issues

    def get_total(self):
        return self.response["total"]

    def get_paging(self):
        return self.response["paging"]

    def get_facets(self):
        return self.response["facets"]