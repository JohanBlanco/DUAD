from flask import Flask, request, abort, jsonify
from task import Task
import db as db
from custom_exeptions import NotFoundError, BadRequestError

app = Flask(__name__)

# Create
@app.route('/tasks/create', methods = ['POST'])
def create_task():
    body = request.json

    if 'title' not in body or 'description' not in body or 'status' not in body:
        raise BadRequestError('There are some missing required fields: name, description or status')

    if not body['title'] or not body['description'] or not body['status']:
        raise BadRequestError('There are some empty fields: name, description or status')

    if body['status'] not in ('Created', 'In progress', 'Needs Changes', 'Completed'):
        raise BadRequestError(f"{body['status']} is an invalid status, the valid statuses are 'Created', 'In progress', 'Needs Changes', 'Completed'")

    task = Task(title=body['title'], description=body['description'], status=body['status'])

    response = db.add_task(task)
    return response, 200
    
# Read
@app.route('/tasks', methods = ['GET'])
def get_tasks():
    # raises an exeption in case it was not found
    task_List = db.get_tasks()
    response = Task.convert_to_dict_list(task_List)
    return response, 200

@app.route('/tasks/<int:id>', methods = ['GET'])
def get_task_by_id(id):
    # raises an exeption in case it was not found
    target:Task = db.get_task(id)

    response = target.__dict__
    return response, 200

# Update
@app.route('/tasks/update/<int:id>', methods = ['POST','PUT'])
def update_task(id):
    body = request.json

    if not body:
        raise BadRequestError(f'No Data was provided')

    if 'status' in body and body['status'] not in ('Created', 'In progress', 'Needs Changes', 'Completed'):
        raise BadRequestError(f"{body['status']} is an invalid status, the valid statuses are Created, In progress, Needs Changes, Completed")

    # raises an exeption in case it was not found
    task_to_update = db.get_task(id)

    if 'title' in body:
        task_to_update.title = body['title']

    if 'status' in body:
        task_to_update.status = body['status']

    if 'description' in body:
        task_to_update.description = body['description']

    response = db.update_task(task_to_update)
    return response, 200

# Delete
@app.route('/tasks/delete/<int:id>', methods = ['DELETE'])
def delete_task(id):
    # raises an exeption in case it was not found
    task_to_delete = db.get_task(id)

    task_to_delete_id = task_to_delete.id

    response = db.delete_task(task_to_delete_id)
    return jsonify(response), 204

# Custom Error Handler
@app.errorhandler(NotFoundError)
def handle_not_found_error(error):
    return jsonify({"error": str(error)}), 404

@app.errorhandler(BadRequestError)
def handle_bad_request_error(error):
    return jsonify({"error": str(error)}), 400

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)