import json
from typing import List, Dict

class TaskManager:
    def __init__(self, file_path: str = "tasks.json"):
        self.file_path = file_path
        self.tasks: List[Dict] = []
        self.next_id = 1 # ID persistente
    
    def add_task(self, title: str, description: str = "") -> None:
        task = {
            "id": self.next_id,
            "title": title,
            "description": description,
            "status": "pending"
        }
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task added: {title}")
    
    def remove_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                print(f"Task removed: {task['title']}")
                return True
        print (f"Task with ID {task_id} not found.")
        return False
    
    def complete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "completed"
                print(f"Task has been completed: {task['title']}")
                return True
        print(f"Task with ID {task_id} not found.")
        return False
    
    def list_tasks(self) -> None:
        if not self.tasks:
            print("No tasks avaiable.")
            return
        for task  in self.tasks:
            status = "✅" if task["status"] == "completed" else "❌"
            print(f"{task['id']}: {task['title']} [{status}] - {task['description']}")
            
    def save_tasks(self) -> None:
        data = {
            "next_id": self.next_id,
            "tasks": self.tasks
        }
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Tasks saved to {self.file_path}")
        
    def load_tasks(self) -> None:
        try:
            with open(self.file_path, "r") as f:
                content = f.read().strip()
                if content:
                    data = json.loads(content)
                    self.tasks = data.get("tasks", [])
                    self.next_id = data.get("next_id", 1)
                else:
                    self.tasks = []
                    self.next_id = 1
            print(f"Tasks loaded from {self.file_path}")
        except FileNotFoundError:
            print(f"No file found at {self.file_path}, starting with empty task list.")
            self.tasks = []
            self.next_id = 1
        except json.JSONDecodeError:
            print(f"file{self.file_path} is corrupted. Starting with empty task list.")
            self.tasks = []
            self.next_id = 1