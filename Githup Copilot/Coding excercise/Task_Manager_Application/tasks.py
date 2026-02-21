from dataclasses import dataclass, asdict
import json
import os
import uuid
from typing import List


@dataclass
class Task:
    id: str
    title: str
    completed: bool = False


class TaskManager:
    def __init__(self, storage_path: str | None = None):
        if storage_path is None:
            storage_path = os.path.join(os.path.dirname(__file__), "tasks.json")
        self.storage_path = storage_path
        self.tasks: List[Task] = []
        self._load()

    def _load(self) -> None:
        try:
            if os.path.exists(self.storage_path):
                with open(self.storage_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.tasks = [Task(**t) for t in data]
            else:
                self.tasks = []
        except (json.JSONDecodeError, OSError) as e:
            raise RuntimeError(f"Failed to load tasks from {self.storage_path}: {e}")

    def _save(self) -> None:
        try:
            # ensure directory exists
            dirpath = os.path.dirname(self.storage_path)
            if dirpath and not os.path.exists(dirpath):
                os.makedirs(dirpath, exist_ok=True)
            with open(self.storage_path, "w", encoding="utf-8") as f:
                json.dump([asdict(t) for t in self.tasks], f, indent=2)
        except OSError as e:
            raise RuntimeError(f"Failed to save tasks to {self.storage_path}: {e}")

    def add_task(self, title: str) -> Task:
        title = (title or "").strip()
        if not title:
            raise ValueError("Task title cannot be empty")
        new = Task(id=str(uuid.uuid4()), title=title)
        self.tasks.append(new)
        self._save()
        return new

    def delete_task(self, task_id: str) -> Task:
        for i, t in enumerate(self.tasks):
            if t.id == task_id:
                removed = self.tasks.pop(i)
                self._save()
                return removed
        raise KeyError(f"Task with id {task_id} not found")

    def complete_task(self, task_id: str) -> Task:
        for t in self.tasks:
            if t.id == task_id:
                if t.completed:
                    return t
                t.completed = True
                self._save()
                return t
        raise KeyError(f"Task with id {task_id} not found")

    def list_tasks(self) -> List[Task]:
        return list(self.tasks)

    def clear_all(self) -> None:
        self.tasks = []
        self._save()
