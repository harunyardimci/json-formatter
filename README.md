# JSON Formatter

## Note that everything in this repo is created by chatGPT. 

Usage:
  json_formatter.py <filename>
  json_formatter.py <json_string>

Examples:
  json_formatter.py data.json
  json_formatter.py '{"name": "John", "age": 30, "city": "New York"}'

Description:
  The JSON Formatter script reads a JSON file or a JSON string, formats it for
  readability, and prints the result to the console. The input can be provided
  as a filename or a JSON string. If a filename is provided, the script will
  read the JSON data from the file. If a JSON string is provided, the script
  will use the string as the input.

  The output is a formatted JSON string, indented with four spaces and sorted
  by keys. If the input is not valid JSON, the script will return an error
  message.

  Examples:
    - To format a JSON file named data.json:
        json_formatter.py data.json

    - To format a JSON string:
        json_formatter.py '{"name": "John", "age": 30, "city": "New York"}'
