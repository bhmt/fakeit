from fastapi import APIRouter
from gen import create_data


class GeneratedRouter(APIRouter):
    base_path: str = '/'

    def __init__(self, paths):
        super().__init__()
        for (key, value) in paths.items():
            super().add_api_route(
                ''.join([self.base_path, key]),
                create_data(value)
            )
