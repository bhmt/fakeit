import sys
from typing import Dict
from . import getter


def check_data(filepath: str) -> object:
    (_data, success) = data(filepath)
    if success is False:
        print(_data)
        sys.exit(-1)

    return _data


def data(filepath: str) -> (object, bool):
    return getter.get_data(filepath)


def check_definitions_mapping(data: object) -> Dict:
    (_definitions_mapping, success) = definitions_mapping(data)
    if success is False:
        print(_definitions_mapping)
        sys.exit(-1)

    return _definitions_mapping


def definitions_mapping(data: object) -> (Dict, bool):
    return getter.get_definitions_mapping(data)
