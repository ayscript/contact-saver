import csv

def save_participant(path, participant_dict):
    """
    Append participant's details to a csv file, writes a header (Name, Age, Phone and Track) if it does not exist
    
    """
    with open(path, 'a+', encoding="utf-8") as f:
        line = f.readlines()
        header = []
        for (key, values) in participant_dict.items():
            header.append(key)
        formatted_header = ",".join(header)
        
        if (f"{formatted_header}\n" not in line):
            f.writelines(f"{formatted_header}\n")
        
        for (key, value) in participant_dict.items():
            f.write(f"{value},")
        f.write('\n')
    
def load_participants(path):
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)

        user_count = 0

        for row_number, row in enumerate(reader):
            if row_number == 0:
                user_count = 0
            else:
                user_count += 1

        print(f"We have {user_count} users in the file!")