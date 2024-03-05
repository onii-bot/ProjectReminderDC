import requests

def set_user_reminder(username, reminder_time, frequency, progress, project):
    data = {
        "username": username,
        "reminder_time": reminder_time,
        "frequency": frequency,
        "progress": progress,
        "project": project
    }
    return requests.post("http://127.0.0.1:8000/api/users/", data=data)