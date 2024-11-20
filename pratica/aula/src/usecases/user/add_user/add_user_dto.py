from pydantic import BaseModel
from uuid import UUID


# INPUT
class AddUserInputDto(BaseModel):
    name: str


# OUTPUT
class AddUserOutputDto(BaseModel):
    id: UUID
    name: str
