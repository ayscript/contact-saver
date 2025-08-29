from pathlib import Path
from file_ops import save_participant
from file_ops import load_participants

workspace = Path('workspace')
workspace.mkdir(exist_ok=True)
file_path = workspace / "contact.csv"

participant_dict = {}

# Name = input("Enter your name: ")
# Age = int(input("Enter your age: "))
# Phone_Number = input("Enter your phone number: ")
# Track = input("Enter your track: ")

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
    try:
        Age = input("Enter age: ")
        if not Age.isdigit():
           raise Exception("enter age")
        else:
            participant_dict['Age'] = int(Age)
    except Exception as e:
        print(e)
        continue
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




# participant_dict['Name'] = input("Enter your name: ")
# participant_dict['Age'] = int(input("Enter your age: "))
# participant_dict['Phone Number'] = input("Enter your phone number: ")
# participant_dict['Track'] = input("Enter your track: ")



save_participant(file_path, participant_dict)
# load_participants(file_path)