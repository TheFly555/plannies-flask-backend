from flask import Flask, request
from flask_smorest import abort
import uuid

app = Flask(__name__)

stores = [{"name": "My Store", "items": [{"name": "pooop", "price": 15.99}]}]



### TODO ENDPOINTS ###
tasks = {
    "1" : {
        "id": 1,
        "description": "voorbeeld taak beschrijving 1",
        "finished": False
    },
    "2" : {
        "id": 2,
        "description": "voorbeeld taak beschrijving 2",
        "finished": False
    }
}

# GET all tasks
@app.get("/tasks")
def get_tasks():
    return {"tasks": list(tasks.values())}

# GET task item
@app.get("/task/<int:task_id>")
def get_task(task_id):
    try:
        return tasks[task_id]
    except KeyError:
        abort(404, message="task not found")

# CREATE task item
@app.post("/task")
def create_task():
    task_data = request.get_json()
    task_id = uuid.uuid4().hex
    task = {**task_data, "id": task_id, "finished": False}
    tasks[task_id] = task
    return task, 201

# UPDATE task item

# DELETE task item

# DELETE list of items

### ACCOUNT ENDPOINTS ###
