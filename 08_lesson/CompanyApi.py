import requests
from config import Config


class Company:
    def __init__(self, token):
        self.token = token
        self.base_url = Config.REQUEST_URL
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title):
        project = {"title": title}
        resp = requests.post(self.base_url + '/api-v2/projects',
                             json=project, headers=self.headers)
        return resp

    def get_project_list(self):
        resp = requests.get(f"{self.base_url}api-v2/projects",
                            headers=self.headers)
        return resp.json()

    def get_project_by_id(self, project_id):
        resp = requests.get(
            self.base_url + '/api-v2/projects/' + project_id,
            headers=self.headers)
        return resp

    def update_project_by_id(self, project_id, new_title=None, deleted=None):
        data = {}
        if new_title is not None:
            data["title"] = new_title
        if deleted is not None:
            data["deleted"] = deleted

        resp = requests.put(f"{self.base_url}/api-v2/projects/"
                            f"{project_id}", json=data, headers=self.headers)
        return resp
