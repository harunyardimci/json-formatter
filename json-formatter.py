import json
import sys

def format_json(json_data):
    try:
        parsed = json.loads(json_data)
        return json.dumps(parsed, indent=4, sort_keys=True)
    except ValueError as e:
        return "Unable to format as JSON: " + str(e)

# Get JSON data from either a file or a command line argument
if len(sys.argv) == 1:
    print("Please provide a filename or JSON string as an argument.")
    sys.exit()
elif len(sys.argv) == 2:
    try:
        with open(sys.argv[1], 'r') as f:
            json_data = f.read()
    except FileNotFoundError as e:
        json_data = sys.argv[1]
else:
    print("Please provide only one filename or JSON string as an argument.")
    sys.exit()

# Format the JSON data and print the result
formatted = format_json(json_data)
print(formatted)

