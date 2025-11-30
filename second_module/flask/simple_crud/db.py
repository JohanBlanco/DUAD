import os
import json
from task import Task
from custom_exceptions import NotFoundError

filepath = 'second_module/flask/simple_crud/tasks.json'

def read_json_file(path = filepath):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return []  # File doesn’t exist or is empty

    with open(path, 'r') as file:
        try:
            json_content = json.load(file)
            return json_content
        except json.JSONDecodeError:
            raise ValueError(f'Invalid JSON file content in {path}')

def write_json_file(dict_content, path = filepath):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)  # ✅ ensure folders exist
        json_string = json.dumps(dict_content, indent=4)
        with open(path, 'w') as file:
            file.write(json_string)
    except Exception as e:
        print(e)

def get_task_next_id():
    task_id = 1
    task_list = get_tasks()
    task_list.sort(key=lambda task: task.id)

    if task_list:
        last_task_id = task_list.pop().id
        task_id = last_task_id + 1
    return task_id

def add_task(task:Task):
    task_list = read_json_file()
    task_id = get_task_next_id()
    task.id = task_id

    task_list.append(task.__dict__)
    write_json_file(task_list)

    return task.__dict__

def get_tasks():
    data =  read_json_file()
    return [Task.from_dict(item) for item in data]

def get_task(id:int):
    task_list = get_tasks()
    filtered_list = list(filter(lambda task: task.id == id, task_list))

    if not filtered_list:
        raise NotFoundError(f"Task with id {id} not found")
    
    return filtered_list[0]

def update_task(task:Task):
    task_list = get_tasks()
    task_to_update:Task = list(filter(lambda t: t.id == task.id, task_list))[0]

    task_to_update.title = task.title
    task_to_update.status = task.status
    task_to_update.description = task.description

    task_list = Task.convert_to_dict_list(task_list)

    write_json_file(task_list)

    return task_to_update.__dict__

def delete_task(id:int):
    task_list = get_tasks()
    task_to_delete:Task = list(filter(lambda t: t.id == id, task_list))[0]

    task_list.remove(task_to_delete)

    task_list = Task.convert_to_dict_list(task_list)

    write_json_file(task_list)

    return ""