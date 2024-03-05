import requests

def delete_user_reminder(username, reminder_id):
    return requests.delete(f"http://127.0.0.1:8000/api/users/{username}/{reminder_id}/")