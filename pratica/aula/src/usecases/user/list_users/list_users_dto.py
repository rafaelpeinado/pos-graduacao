from pydantic import BaseModel
from typing import List
from uuid import UUID

# INPUT
class ListUsersInputDto(BaseModel):
    pass
    

# DTO INTERMEDIÁRIO
class UserDto(BaseModel):
    id: UUID
    name: str


# OUTPUT
class ListUsersOutputDto(BaseModel):
    users: List[UserDto]

