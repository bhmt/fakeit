from models.definition import Definition
from models.dummy import Dummy
from typing import Callable, Union
import rand


def base(name: str, value: Union[bool, str, float, list]):
    if name:
        d = Dummy()
        d.__setattr__(name, value)
        return d
    return value


def boolean(definition: Definition) -> Union[Dummy, bool]:
    value: bool = rand.boolean()
    return base(definition.name, value)


def number(definition: Definition) -> Union[Dummy, float]:
    value = rand.number(interval=definition.interval)
    return base(definition.name, value)


def string(definition: Definition) -> Union[Dummy, str]:
    value = rand.string(interval=definition.interval)
    return base(definition.name, value)


def array(definition: Definition) -> Union[Dummy, bool, str, float, list]:
    deconstruct = definition.type.split(":")
    inner_interval = ':'.join(deconstruct[2:])

    value = rand.array(
        _type=deconstruct[1],
        inner_interval=inner_interval,
        interval=definition.interval
    )

    return base(definition.name, value)


def obj(definition: Definition):
    ...


def create_data(definition: Definition) -> Callable:
    def switch() -> Union[Dummy, bool, str, list, float]:
        t = definition.type.split(":")[0]
        return {
            "boolean": boolean,
            "number": number,
            "string": string,
            "array": array,
            "objet": obj
        }.get(t)(definition)

    return switch
