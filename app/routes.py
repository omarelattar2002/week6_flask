
from list.tasks import tasks_list
from . import app


@app.route("/")
def index():
    hello = "Hello world"
    return hello

@app.route("/tasks")
def get_tasks():
    return tasks_list

@app.route("/tasks/<int:task_id>")
def get_task(task_id):
    for task in tasks_list:
        if task['id'] == task_id:
            return task
    return {'error':'The task you are looking for cannot be found'},404
