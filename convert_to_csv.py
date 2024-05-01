import pandas as pd
import re
#This parses out names from the input file
def parse_text(filename):
    data = {}
    current_name = None
    with open(filename, 'r') as file:
        for line in file:
            # Use regular expression to find capitalized names
            match = re.match(r'^([A-Z][A-Z\s\']+),\s*([A-Z][A-Z\s\-\']+(?: [A-Z]\.)?)', line)
            if match:
                # If a name is found, update current_name
                current_name = match.group().strip() #Stores name as the key to the dict
                data[current_name] = line[match.end():].strip() #Stores remaining from line into dict value
            elif current_name is not None:
                # If current_name is not None, append the line to the corresponding text
                data[current_name] += line.strip()
    return data #Returns dictionary with key: Congressman names, Value: rest of string up until next name

def remove_invalid_pages(dictionary):
    #Removes dictionary value with page numbers starting with A or E.
    pattern = re.compile(r'[AE]\d{4}')
    keys_to_delete = []
    for key, val in dictionary.items():
      if pattern.search(val):
        keys_to_delete.append(key)
    for key in keys_to_delete:
      del dictionary[key]
    return dictionary

def main():
    filename = '<Insert filepath here>'
    dictionary = parse_text(filename)
    valid_entries = remove_invalid_pages(dictionary)
    # Todo: Finish parsing data to get end up with a csv with columns: Name, Topic, Subtopic, Date, Page Number, and Remarks.
    # (Currently have name and removed pages starting with A and E.)
    # Also need to change it to have an input file directory just like auto_convert_py.
    return valid_entries



if __name__ == "__main__":
    main()
