import requests
from server.base import BASE_URI

def delete_user_reminder(username, reminder_id):
    return requests.delete(f"{BASE_URI}/api/users/{username}/{reminder_id}/")