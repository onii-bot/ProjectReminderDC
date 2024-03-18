import requests
from server.base import BASE_URI

def get_projects():
    projects = requests.get(f"{BASE_URI}/api/projects/").json()
    projects_dict = {
    }
    for project in projects:
        projects_dict[project['id']] = project
    return projects_dict

def get_user_reminders(user):
    data = requests.get(f"{BASE_URI}/api/users/{user}").json()
    return data