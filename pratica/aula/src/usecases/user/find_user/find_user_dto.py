from typing import List
from pydantic import BaseModel
from uuid import UUID

# INPUT
class FindUserInputDto(BaseModel):
    id: UUID


class TaskOutputDto(BaseModel):
    id: UUID
    title: str
    description: str
    completed: bool


# OUTPUT
class FindUserOutputDto(BaseModel):
    id: UUID
    name: str
    tasks: List[TaskOutputDto]
    pending_tasks: int
    