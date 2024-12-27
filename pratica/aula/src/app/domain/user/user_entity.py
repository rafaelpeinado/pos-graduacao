from uuid import UUID, uuid4
from typing import List
from app.domain.task.task_entity import Task

class User:

    id: UUID
    name: str
    tasks: List[Task]

    def __init__(self, id: UUID, name: str):
        self.id = id
        self.name = name
        self.tasks = []
        self.validate()

    def validate(self):
        if not isinstance(self.id, UUID):
            raise Exception("id must be an UUID.")
        if not (isinstance(self.name, str) and len(self.name) > 0):
            raise Exception("name is required.")
        
    def collect_tasks(self, tasks: List[Task]) -> None:
        self.tasks.extend(tasks)

