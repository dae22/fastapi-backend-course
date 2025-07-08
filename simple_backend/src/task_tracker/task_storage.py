import json

class TaskStorage:
    def __init__(self, file_path='database.json'):
        self.file_path = file_path

    def read_tasks(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return dict()

    def write_tasks(self, tasks):
        with open(self.file_path, 'w') as file:
            json.dump(tasks, file)

    def add_task(self, task_description):
        tasks = self.read_tasks()
        new_id = len(tasks)
        tasks[str(new_id)] = {'task': task_description, 'status': False}
        self.write_tasks(tasks)
        return new_id

    def update_task(self, task_id, new_status=True):
        tasks = self.read_tasks()
        if str(task_id) in tasks:
            tasks[str(task_id)]['status'] = new_status
            self.write_tasks(tasks)
            return True
        return False

    def delete_task(self, task_id):
        tasks = self.read_tasks()
        if str(task_id) in tasks:
            del tasks[str(task_id)]
            self.write_tasks(tasks)
            return True
        return False