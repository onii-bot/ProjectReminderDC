import requests
from server.base import BASE_URI

def set_user_reminder(username, reminder_time, frequency, progress, project):
    data = {
        "username": username,
        "reminder_time": reminder_time,
        "frequency": frequency,
        "progress": progress,
        "project": project
    }
    return requests.post(f"{BASE_URI}/api/users/", data=data)