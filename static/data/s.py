import os
import json

# Get the current directory
current_directory = os.getcwd()

# Get all JSON files in the current directory
json_files = [file for file in os.listdir(current_directory) if file.endswith(".json")]

total = 0

# Iterate through each JSON file
for file in json_files:
    file_path = os.path.join(current_directory, file)
    with open(file_path, "r") as f:
        data = json.load(f)
        num_elements = len(data)
        print(f"Number of elements in {file}: {num_elements}")
        total += num_elements

print(f"Total number of elements: {total}")
