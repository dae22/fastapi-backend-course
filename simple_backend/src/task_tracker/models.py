import requests


class TaskStorage:
    new_id = 0

    def __init__(self):
        self.url = "https://686d861bc9090c4953868efa.mockapi.io/tasks"

    def read_tasks(self):
        response = requests.get(self.url)
        return response.json()

    def add_task(self, task_description, solution):
        task = {"task": task_description, "solution": solution, "status": False, "id": self.new_id}
        self.new_id += 1
        requests.post(self.url, json=task)
        return self.new_id - 1

    def update_task(self, task_id, new_status=True):
        response = requests.patch(f'{self.url}/{task_id}', json={"status": new_status})
        return response.ok

    def delete_task(self, task_id):
        response = requests.delete(f'{self.url}/{task_id}')
        return response.ok


class Cloudflare:
    def __init__(self):
        self.url = "https://api.cloudflare.com/client/v4/accounts/9da3e3c5869ff2a1a4565edbb552d270/ai/run/@cf/meta/llama-3-8b-instruct"
        self.headers = {"Authorization": "Bearer xW7wjmZGc3_3CEsCgPwCKx6D-ROE3-gL6aaltaQ_"}

    def ask_solution(self, task_description):
        json_message = {"messages": [
            {"role": "system", "content": "You are a friendly assistant that helps solve the task"},
            {"role": "user",
             "content": f"Please advise haw i can solve this task: {task_description}"}
        ]}
        response = requests.post(self.url, headers=self.headers, json=json_message)
        return response.json()
