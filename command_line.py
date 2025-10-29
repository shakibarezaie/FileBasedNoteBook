import user
import note



def displayـuser_status():
    current_user = user.get_current_user()
    if current_user:
        print(current_user, end = '')
    print('>', end = '')



def sign_up_command():
    print("username: ", end = '')
    username = input().strip()
    print("password: ", end = '')
    password = input().strip()

    error = user.sign_up(username, password)
    if error is not None:
        print(f"sign up failed: {error}")
    else: 
        print("signed up successfully.")



def login_command():
    print("username: ", end = '')
    username = input().strip()
    print("password: " , end = '')
    password = input().strip()

    error = user.login(username, password)
    if error is not None: 
        print(f"login failed: {error}")
    else:
        print("logged in successfully.")



def logout_command():
    user.logout()
    print("logged out successfully.")



def exit_command(): 
    quit()



def login_required(command_function):
    """this function can only be called if the user is logged in"""
    def login_required_command():
        username = user.get_current_user()
        if username is None:
            print("you need to be logged in first.")
            return
        command_function(username)
    return login_required_command 



def create_note_command(username: str): 
    print("please enter your text: ")
    text = input().strip()

    note.create_note(username, text)
    print("your note has been successfully created.")



def list_notes_command(username: str):
    user_notes = note.list_notes(username)
    for item in user_notes:
        print(f"{item['index']}: {item['note'][:7]}...")


def read_note_command(username: str):
    print("note No. : ", end = '')
    try:
        note_number = int(input())
    except ValueError: 
        print("invalid note number.")
        return
    
    print(note.read_note(username, note_number))



def append_text_command(username: str):
    try:
        print("note No. : ", end = '')
        note_number = int(input())
    except ValueError:
        print("invalid note number.")
        return
    
    print("please enter your text: ")
    text = input().strip()

    note.append_notes(username, note_number, text)
    print("your text has been successfully appended.")



def edit_note_content_command(username: str):
    print("note No. : ", end = '')
    try:
        note_number = int(input())
    except ValueError:
        print("invalid note number.")

    print("please enter your text: ")
    text = input().strip()

    note.edit_note_content(username, note_number, text)
    print("your note has been successfully editted.")



def add_text_to_note_command(username: str):
    print("please enter your text: ")
    text = input().strip()
    print("note No. : ", end = '')
    try:
        note_number = int(input())
    except ValueError:
        print("invalid note number.")
        return
    
    print("index to add the text: ", end = '')
    try: 
        index = int(input())
    except Exception:
        print("invalid index")
        return
    
    note.add_text_to_note(username, note_number, index, text)
    print("your note has been successfully editted.")



def remove_text_from_note_command(username: str):
    print("note No. : ", end = '')
    try:
        note_number = int(input())
    except ValueError:
        print("invalid note number.")
        return
    
    print("index to remove the text: ", end = '')
    try:
        position = int(input()) 
    except ValueError:
        print("invalid index.")
        return
    
    print("length of text to remove: ", end = '')
    try:
        length = int(input())
    except ValueError:
        print("invalid length.")
        return
    
    note.remove_text_from_note(username, note_number, length, position)
    print("your note has been successfully editted.")



def delete_note_command(username: str):
    try:
        print("note No. : ", end = '')
        note_number  = int(input())
        print("your note has been successfully deleted.")
    except ValueError:
        print("invalid note number")  

    note.delete_note(username, note_number)


def menu():
    print("available commands:")
    index = 1
    for command in COMMAND_HANDLERS: 
        print(index, '. ', command, sep='')
        index += 1
    print("please enter the command: ")


COMMAND_HANDLERS = {
    'login': login_command,
    'sign up': sign_up_command,
    'logout': logout_command, 
    'exit': exit_command,
    'create new note': login_required(create_note_command),
    'view all notes': login_required(list_notes_command),
    'read note': login_required(read_note_command),
    'append to note': login_required(append_text_command),
    'edit note': login_required(edit_note_content_command),
    'add text to note': login_required(add_text_to_note_command),
    'remove text from note': login_required(remove_text_from_note_command),
    'delete note': login_required(delete_note_command)
    }



def command_handler():
    new_command = input()
    if not new_command:
        return
    if new_command not in COMMAND_HANDLERS: 
        print("invalid command.")
        return
    
    COMMAND_HANDLERS[new_command]()


def setup_environment():
    user.load_users_data()
    note.load_user_notes()

    menu()

    while True:
        displayـuser_status()
        command_handler()

if __name__ == '__main__':
    setup_environment()

