import os
import json
from typing import Optional



USERS_INFO = {}
USERS_INFO_DATA_FILE = './users.json'

CURRENT_USER: Optional[str] = None



def save_user_info():
    """save users data to file."""
    with open(USERS_INFO_DATA_FILE, 'w') as file:
        json.dump(USERS_INFO, file)



def load_users_data():
    """load users data from file."""
    global USERS_INFO

    if os.path.exists(USERS_INFO_DATA_FILE):
        with open(USERS_INFO_DATA_FILE) as file: 
            USERS_INFO = json.load(file)



def sign_up(username: str, password: str) -> Optional[str]:
    global USERS_INFO

    if username in USERS_INFO:
        return "this username is already taken."

    USERS_INFO[username] = {
        'password': password
    }
    save_user_info()
    


def login(username: str, password: str) -> Optional[str]:
    global CURRENT_USER

    if username not in USERS_INFO:
        return "username not found."

    info = USERS_INFO[username]

    if info['password'] != password:
        return "the entered password is incorrect"
    
    CURRENT_USER = username
    return 



def logout():
    global CURRENT_USER

    CURRENT_USER = None



def get_current_user():
    return CURRENT_USER
