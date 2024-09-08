import json

# Read JSON data from a file
with open('input.json', 'r') as file:
    data = json.load(file)

# Print in a human-readable format
print(json.dumps(data, indent=4))
