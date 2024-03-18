import requests
from server.base import BASE_URI

def edit_user_reminder(username, reminder_time, frequency, progress, project, reminder_id):
    data = {
        "username": username,
        "reminder_time": reminder_time,
        "frequency": frequency,
        "progress": progress,
        "project": project
    }
    return requests.put(f"{BASE_URI}/api/users/{username}/{reminder_id}/", data=data)