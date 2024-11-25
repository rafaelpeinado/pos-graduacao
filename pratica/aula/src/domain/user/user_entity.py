from uuid import UUID, uuid4
from typing import List
from domain.task.task_entity import Task

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
            raise Exception("id must be an UUID")
        if not isinstance(self.name, str) or len(self.name) == 0:
            raise Exception("name is required") 
        
    def collect_tasks(self, tasks: List[Task]) -> None:
        self.tasks.extend(tasks)

    def count_pending_tasks(self) -> int:
        count = 0
        for task in self.tasks:
            if task.completed is not True:
                count += 1
        return count





# usuario_1 = User(id=uuid4(), name="Vitória")
# usuario_2 = User(id=uuid4(), name="Alexandre")

# usuario_1.name # Vitória
# usuario_2.name # Alexandre


# usuario_3 = User(id=4, name="sou um usuário inválido")

# usuario_3.validate() # ERRO: id must be an UUID

# usuario_4 = User(id=5, name="Roney") # ERRO: id must be an UUID
