import json
import argparse
import os

def format_json(json_data):
    try:
        parsed = json.loads(json_data)
        return json.dumps(parsed, indent=4, sort_keys=True)
    except ValueError as e:
        return "Unable to format as JSON: " + str(e)

# Parse command line arguments
parser = argparse.ArgumentParser(description='JSON Formatter.')
parser.add_argument('json_input', metavar='<json_input>', type=str,
                    help='the JSON file or string to format')
args = parser.parse_args()

# Get JSON data from either a file or a command line argument
if os.path.isfile(args.json_input):
    with open(args.json_input, 'r') as f:
        json_data = f.read()
else:
    json_data = args.json_input

# Format the JSON data and print the result
formatted = format_json(json_data)
print(formatted)
