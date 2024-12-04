import requests
from setting import LOGIN, PASSWORD, COMPANY_ID


class Yougile:
    def __init__(self):
        self.login = LOGIN
        self.password = PASSWORD
        self.company_id = COMPANY_ID
        self.url = "https://ru.yougile.com/"

    def get_auth_key(self):
        payload = {
            "login": self.login,
            "password": self.password,
            "companyId": self.company_id }
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post((self.url+'api-v2/auth/keys/get'), json=payload, headers=headers)
        #response.raise_for_status()
        return response.json()[0]["key"]


    def create_project(self, name):
        auth_headers = {
          'Authorization': f'Bearer {self.get_auth_key()}',
           'Content-Type': 'application/json'
        }
        title = {
            "title": name
    }
        resp = requests.post((self.url + '/api-v2/projects'), headers=auth_headers, json=title)
        return resp

    def get_all_projects(self):
        auth_headers = {
            'Authorization': f"Bearer {self.get_auth_key()}",
            'Content-Type': 'application/json'
        }
        projects = requests.get(f"{self.url}/api-v2/projects", headers=auth_headers)
        return projects

    def get_project_by_id(self, project_id):
        auth_headers = {
            'Authorization': f"Bearer {self.get_auth_key()}",
            'Content-Type': 'application/json'
        }
        project = requests.get(f"{self.url}/api-v2/projects/{project_id}", headers=auth_headers)
        return project

    def update_project_title(self, name, project_id):
        auth_headers = {
            'Authorization': f"Bearer {self.get_auth_key()}",
            'Content-Type': 'application/json'
        }
        title = {
            "title": name
        }
        project = requests.put(f"{self.url}/api-v2/projects/{project_id}", json=title, headers=auth_headers)
        return project
