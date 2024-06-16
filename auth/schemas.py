from typing import Optional
from pydantic.version import VERSION as PYDANTIC_VERSION
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    grz: str
    team: str
    photo: str
    number_phone: str
    email: str
    car_model: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True

class UserCreate(schemas.BaseUserCreate):
    username: str
    grz: str
    team: str
    photo: str
    number_phone: str
    car_model:str
    email: str
    password: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserUpdate(schemas.BaseUserUpdate):
    username: str
    grz: str
    team: str
    photo: str
    number_phone: str
    car_model: str
