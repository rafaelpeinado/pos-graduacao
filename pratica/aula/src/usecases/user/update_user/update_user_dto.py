from pydantic import BaseModel
from uuid import UUID

# INPUT
class UpdateUserInputDto(BaseModel):
    id: UUID


#OUTPUT 
class UpdateUserOutputDto(BaseModel):
    id: UUID
    name: str
