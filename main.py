from pathlib import Path
from file_ops import save_participant
from file_ops import load_participants

workspace = Path('workspace')
workspace.mkdir(exist_ok=True)
file_path = workspace / "contact.csv"

participant_dict = {}

while True:
    while True:
        try:
            Name = input("Enter name: ")
            if not Name.isalpha():
                raise Exception("enter alphabet")
            else:
                participant_dict['Name'] = Name
        except Exception as e:
            print(e)
            continue
        break
    while True:
        try:
            Age = input("Enter age: ")
            if not Age.isdigit():
                raise Exception("enter age")
            else:
                participant_dict['Age'] = int(Age)
        except Exception as e:
            print(e)
            continue
        break

    while True:
        try:
            phonenumber = input("Enter phone number: ")
            if not Age.isdigit():
                raise Exception("phone number must be in digit")
            elif len(phonenumber) != 11:
                raise Exception("phone number must be 11 digits")
            else:
                participant_dict['phone number'] = phonenumber
        except Exception as e:
            print(e)
            continue
        break
    while True:
        try:
            Track = input("Enter track: ")
            if not Name.isalpha():
                raise Exception("track must be in alphabet")
            else:
                participant_dict['track'] = Track
        except Exception as e:
            print(e)
            continue
        break
    user_exit = input("Do you want to exit?\n1.\tYes\n2.\tNo\n\n")
    if user_exit == '1':
        break




save_participant(file_path, participant_dict)

load_participants(file_path)