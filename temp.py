import requests
username = "thenooboi"
def set_user_reminder():
    data = {
        "username": username,
        "reminder_time":"10pm",
        "frequency":"weekly",
        "progress": "None",
        "project":1
    }
    return requests.put("http://127.0.0.1:8000/api/users/noob/1/", data=data)

set_user_reminder()