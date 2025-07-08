from fastapi import FastAPI

app = FastAPI()

tasks = dict()
next_id = 0


@app.get("/tasks")
def get_tasks():
    return {'List of tasks': tasks}


@app.post("/tasks")
def create_task(task):
    global next_id
    new_task = {'task': task, 'status': False}
    tasks[next_id] = new_task
    next_id += 1
    return {'message': f'New task added. Assigned id: {next_id - 1}'}


@app.put("/tasks/{task_id}")
def update_task(task_id: int):
    if task_id in tasks.keys():
        tasks[task_id]['status'] = True
        return {'message': 'Task marked as completed'}
    else:
        return {'message': 'Task not found'}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id in tasks.keys():
        del tasks[task_id]
        return {'message': 'Task deleted'}
    else:
        return {'message': 'Task not found'}
