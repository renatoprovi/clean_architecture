from pydantic import BaseModel
from typing import List
from uuid import UUID


class ListUsersInputDto(BaseModel):
    pass


class UserDto(BaseModel):
    id: UUID
    name: str


class ListUsersOutputDto(BaseModel):
    users: List[UserDto]

# user_dto = UserDto(id=1, name='Renato') # erro (BaseModel vai valiodar)
# user_dto = UserDto(id=uuid4(), name='Renato') # Não vai dar erro (BaseModel vai validar)
