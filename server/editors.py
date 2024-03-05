import requests

def edit_user_reminder(username, reminder_time, frequency, progress, project, reminder_id):
    data = {
        "username": username,
        "reminder_time": reminder_time,
        "frequency": frequency,
        "progress": progress,
        "project": project
    }
    return requests.put(f"http://127.0.0.1:8000/api/users/{username}/{reminder_id}/", data=data)