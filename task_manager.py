class Task:
    def __init__(self, task_id: int, description: str):
        self.id = task_id
        self.description = description
        self.completed = False

    def __repr__(self):
        status = "✅" if self.completed else "❌"
        return f"[{status}] ({self.id}) {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description: str) -> dict:
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        return vars(task)

    def remove_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False

    def edit_task(self, task_id: int, new_description: str) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                task.description = new_description
                return True
        return False

    def complete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                return True
        return False

    def filter_tasks(self, status: str = "all") -> list:
        if status == "done":
            return [vars(t) for t in self.tasks if t.completed]
        elif status == "pending":
            return [vars(t) for t in self.tasks if not t.completed]
        return [vars(t) for t in self.tasks]