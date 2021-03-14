from random import uniform, random, randrange, choice
from typing import Union
import string

letters = string.ascii_letters
default_interval = 10


def __parse_string_interval__(interval: str) -> (int, int):
    _min, _max = 0, 0
    if isinstance(interval, str):
        elements = [e for e in interval.split(":") if e != ""]
        if len(elements) == 1:
            elements = int(elements[0])
            if elements < 0:
                _min = elements
            _max = elements
        else:
            elements = sorted(map(int, elements))
            _min, _max = elements[0], elements[1]
    return _min, _max


def boolean() -> bool:
    return choice([True, False])


def number(interval: Union[str, int] = None) -> float:
    if interval is None:
        return random()
    if isinstance(interval, str):
        _min, _max = __parse_string_interval__(interval)
        return uniform(_min, _max)
    if interval < 0:
        return uniform(interval, 0)
    return uniform(0, interval)


def string(interval: Union[str, int] = None) -> str:
    str_length = interval or default_interval
    if isinstance(interval, str):
        _min, _max = __parse_string_interval__(interval)
        str_length = int(uniform(_min, _max))
    return ''.join(choice(letters) for _ in range(str_length))


def array(_type: str, inner_interval: Union[str, int] = default_interval, interval: Union[str, int] = default_interval) -> list:
    _min_len, _max_len = 0, default_interval

    if isinstance(interval, str):
        _min_len, _max_len = __parse_string_interval__(interval)
    else:
        _max_len = int(interval)

    array_length = randrange(_min_len, _max_len)

    if _type == 'string':
        return [string(inner_interval) for _ in range(array_length)]
    return [number(inner_interval) for _ in range(array_length)]
