import json
from models.definition import Definition
from typing import Dict, Union


class JsonObject:
    def __init__(self, dictionary: dict):
        vars(self).update(dictionary)

    def to_json(self) -> str:
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=True, indent=2)


def get_definitions_mapping(data: object) -> (Union[Dict[str, Definition], str], bool):
    route_definition_map = dict()
    msg = []

    check_paths = data.__dict__.get("paths")
    check_keys = check_paths.__dict__.keys() if check_paths else None
    if not check_paths or not check_keys:
        return ("paths must be defined", False)

    for (key, value) in data.paths.__dict__.items():
        try:
            route_definition_map[key] = Definition(
                type=value.type,
                name=value.__dict__.get("name"),
                interval=value.__dict__.get("interval"),
                model=value.__dict__.get("model")
            )

        except (AttributeError, ValueError) as e:
            msg.append(f"In route {key} : {e}")

    if msg:
        return ("\n".join(msg), False)
    return (route_definition_map, True)


def get_obj(data: str) -> (object, bool):
    try:
        return (json.loads(data, object_hook=JsonObject), True)
    except ValueError:
        return ("Could not parse json.", False)


def get_data(filepath: str) -> (object, bool):
    try:
        with open(filepath) as f:
            _json: str = f.read()
            return get_obj(_json)
    except FileNotFoundError:
        return (f"File '{filepath}' does not exist.", False)
