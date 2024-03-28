from flask import render_template, request
from list.tasks import tasks_list
from . import app


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/users', methods = ['POST'])
def create_user():
    if not request.is_json:
        return {'error': 'Your content-type must be application/json'}, 400
    data = request.json

    required_fields = ['first_name', 'last_name', 'username', 'email', 'password']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)
        if missing_fields:
            return {'error':f"{', '.join(missing_fields)} must be in the request body"}, 400
        return 'This is the create user endpoint'

@app.route("/tasks")
def get_tasks():
    return tasks_list

@app.route("/tasks/<int:task_id>")
def get_task(task_id):
    for task in tasks_list:
        if task['id'] == task_id:
            return task
    return {'error':'The task you are looking for cannot be found'},404


