import requests

class SnykAPI:
    base_url = "https://api.snyk.io/rest/orgs"
    api_version = "2024-10-15"

    def __init__(self, api_token):
        self.headers = {
            'Authorization': f'token {api_token}',
            'Content-Type': 'application/vnd.api+json'
        }

    def get_issues(self, org_id, project_id):
        """
        Fetches issues from Snyk for a specific organization and project.

        :param org_id: The Snyk organization ID
        :param project_id: The Snyk project ID
        :return: JSON response containing the issues
        """
        url = f"{self.base_url}/{org_id}/issues?version={self.api_version}&scan_item.type=project&scan_item.id={project_id}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching issues: {e}")
            return None
    
    def get_orgs(self):
        """
        Fetches organizations from Snyk.

        :return: JSON response containing the organizations
        """
        url = f"https://api.snyk.io/rest/orgs?version={self.api_version}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching organizations: {e}")
            return None