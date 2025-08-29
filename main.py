from pathlib import Path
from file_ops import save_participant
from file_ops import load_participants

workspace = Path('workspace')
workspace.mkdir(exist_ok=True)
file_path = workspace / "contact.csv"

participant_dict = {}

participant_dict['Name'] = input("Enter your name: ")
participant_dict['Age'] = input("Enter your age: ")
participant_dict['Phone Number'] = input("Enter your phone number: ")
participant_dict['Track'] = input("Enter your track: ")


save_participant(file_path, participant_dict)
# load_participants(file_path)