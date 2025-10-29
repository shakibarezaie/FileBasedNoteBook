import os
import json
from typing import Optional
from collections import defaultdict



USERS_NOTES = defaultdict(list) 
NOTES_DATA_FILE = './notes.json'


def save_user_notes():
    """save users data to file."""
    with open(NOTES_DATA_FILE, 'w') as file:
        json.dump(USERS_NOTES, file)



def load_user_notes():
    """load user notes from file."""
    global USERS_NOTES

    if os.path.exists(NOTES_DATA_FILE):
        with open(NOTES_DATA_FILE) as file: 
            USERS_NOTES = defaultdict(list, json.load(file))



def create_note(username: str, text: str):
    global USERS_NOTES

    user_notes = USERS_NOTES[username]
    notes_number = len(user_notes)
    user_notes.append({
        'note': text,
        'index': notes_number + 1
    })

    save_user_notes()



def list_notes(username: str):
    return USERS_NOTES[username]



def read_note(username: str, index: int) -> str: # No: number of the note
    global USERS_NOTES

    user_notes = USERS_NOTES[username]
    if index < 1 or index > len(user_notes): 
        return "invalid note number."

    if type(user_notes[index - 1]) == dict and 'note' in user_notes[index - 1]:
        return user_notes[index - 1]['note']
    else:
        return "error."



def append_notes(username: str, index: int, text: str) -> Optional[str]:
    global USERS_NOTES

    user_notes = USERS_NOTES[username]
    if index < 1 or index > len(user_notes):
        return "invalid note number."
    
    current_note = user_notes[index - 1]
    current_note['note'] += " " + text

    save_user_notes()



def edit_note_content(username: str , index: int, new_note: str):
    global USERS_NOTES

    user_notes = USERS_NOTES[username]
    if index < 1 or index > len(user_notes):
        return "invalid id."
    user_notes[index - 1]['note'] = new_note

    save_user_notes()


def add_text_to_note(username: str, No: int, index: int, text: str):
    global USERS_NOTES

    user_notes = USERS_NOTES[username]

    if No < 1 or No > len(user_notes):
        return "invalid id."
    
    note = user_notes[No - 1]

    if index < 0 or index > len(note['note']):
        return "invalid position."
    
    updated_note = note['note'][:index] + text + note['note'][index:]
    note['note'] = updated_note

    save_user_notes()



def remove_text_from_note(username: str, No: int, length: int, position: int):
    global USERS_NOTES

    user_notes = USERS_NOTES[username]

    if No < 1 or No > len(user_notes):
        return "invalid note number."
 
    note = user_notes[No - 1]

    if position < 0 or position > len(note['note']):
        return "invalid position."
    
    if length < 0 or position + length > len(note['note']):
        return "invalid length."
    
    new_note = note['note'][:position] + note['note'][position + length:]
    note['note'] = new_note

    save_user_notes()


def delete_note(username: str, No: int):
    user_notes = USERS_NOTES[username]

    if No < 1 or No > len(user_notes):
        return "invalid note number."

    del USERS_NOTES[username][No - 1]

    save_user_notes()


        
