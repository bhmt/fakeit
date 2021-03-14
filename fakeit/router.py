from fastapi import APIRouter
from typing import Callable
from models.dummy import Dummy
import rand


class GeneratedRouter(APIRouter):
    base_path: str = '/'

    def __init__(self, paths):
        super().__init__()
        for (key, value) in paths.__dict__.items():
            super().add_api_route(
                ''.join([self.base_path, key]),
                self.create_data(value),
                response_model=Dummy
            )

    def create_data(self, value: object) -> Dummy:
        def new() -> Dummy:
            d = Dummy()
            d.__setattr__("number", rand.number("30:50"))
            d.__setattr__("string", rand.string(36))
            return d

        return new
