import json

def read_json_file(path='week_17/data.json'):
    with open(path) as file:
        string_content = file.read()
        json_content = json.loads(string_content)
        return json_content

def write_file(content, path='week_17/data.json'):
    with open(path, 'w') as file:
        file.write(content)