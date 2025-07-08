from fastapi import FastAPI
from task_storage import TaskStorage

app = FastAPI()
task_storage = TaskStorage()


@app.get("/tasks")
def get_tasks():
    data = task_storage.read_tasks()
    return {'List of tasks': data}


@app.post("/tasks")
def create_task(task):
    index = task_storage.add_task(task)
    return {'message': f'New task added. Assigned id: {index}'}


@app.put("/tasks/{task_id}")
def update_task(task_id: int):
    if task_storage.update_task(task_id):
        return {'message': 'Task status update'}
    return {'message': 'Task not found'}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_storage.delete_task(task_id):
        return {'message': 'Task deleted'}
    return {'message': 'Task not found'}
