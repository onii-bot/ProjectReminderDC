import requests

def get_projects():
    projects = requests.get("http://127.0.0.1:8000/api/projects/").json()
    projects_dict = {
    }
    for project in projects:
        projects_dict[project['id']] = project
    return projects_dict

def get_user_reminders(user):
    data = requests.get(f"http://127.0.0.1:8000/api/users/{user}").json()
    return data