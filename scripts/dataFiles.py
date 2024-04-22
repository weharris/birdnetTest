import os

def get_file_names(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Usage
file_names = get_file_names('data/')
# Prompt the user for the directory path
directory = input("Please enter the directory path: ")

# Get the file names
file_names = get_file_names(directory)