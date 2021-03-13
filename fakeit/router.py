from fastapi import APIRouter
from pydantic import BaseModel
import random
import string

letters = string.ascii_letters


class Dummy(BaseModel):
    class Config:
        orm_mode = True
        extra = 'allow'


def create_data(values) -> Dummy:

    d = Dummy()
    d.__setattr__("number", random.random())
    d.__setattr__("string", ''.join(random.choice(letters) for i in range(10)))
    return d


class GeneratedRouter(APIRouter):
    base_path: str = '/'

    def __init__(self, paths):
        super().__init__()
        for (key, value) in paths.__dict__.items():
            super().add_api_route(
                ''.join([self.base_path, key]),
                create_data(value),
                response_model=Dummy
            )
