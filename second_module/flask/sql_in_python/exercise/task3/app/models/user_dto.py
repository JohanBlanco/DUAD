from pydantic import BaseModel

class UpdateUserDto(BaseModel):
    id:int
    first_name: str
    last_name: str
    email: str
    username: str
    birthdate: str
    status: str

class CreateUserDto(BaseModel):
    first_name: str
    last_name: str
    email: str
    username: str
    password: str
    birthdate: str
    status: str
