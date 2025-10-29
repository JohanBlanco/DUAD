import json

def read_json_file(path):
    with open(path) as file:
        string_content = file.read()
        json_content = json.loads(string_content)
        return json_content

def write_file(dict_content, path):
    json_string = json.dumps(dict_content, indent=4)
    with open(path, 'w') as file:
        file.write(json_string)