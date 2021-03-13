import json


class JsonObject:
    def __init__(self, dictionary: dict):
        vars(self).update(dictionary)

    def to_json(self) -> str:
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=True, indent=2)


def get_obj(data: str) -> (object, bool):
    try:
        return (json.loads(data, object_hook=JsonObject), True)
    except ValueError as e:
        return ("Could not parse json.", False)


def get_data(filepath: str) -> (object, bool):
    try:
        with open(filepath) as f:
            _json: str = f.read()
            return get_obj(_json)
    except FileNotFoundError as e:
        return (f"File '{filepath}' does not exist.", False)
