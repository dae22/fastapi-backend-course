from http.client import responses

import requests


class TaskStorage:
    new_id = 0

    def __init__(self):
        self.url = "https://686d861bc9090c4953868efa.mockapi.io/tasks"

    def read_tasks(self):
        response = requests.get(self.url)
        return response.json()

    def write_task(self, task):
        requests.post(self.url, json=task)

    def add_task(self, task_description):
        task = {"task": task_description, "status": False, "id": self.new_id}
        self.new_id += 1
        self.write_task(task)
        return self.new_id - 1

    def update_task(self, task_id, new_status=True):
        response = requests.patch(f'{self.url}/{task_id}', json={"status": new_status})
        return response.ok

    def delete_task(self, task_id):
        response = requests.delete(f'{self.url}/{task_id}')
        return response.ok
