from models.definition import Definition
from models.base import Base
from typing import Callable, Union
import rand


def base(name: str, value: Union[bool, str, float, list]):
    if name:
        d = Base()
        d.__setattr__(name, value)
        return d
    return value


def boolean(definition: Definition) -> Union[Base, bool]:
    value: bool = rand.boolean()
    return base(definition.name, value)


def number(definition: Definition) -> Union[Base, float]:
    value = rand.number(interval=definition.interval)
    return base(definition.name, value)


def string(definition: Definition) -> Union[Base, str]:
    value = rand.string(interval=definition.interval)
    return base(definition.name, value)


def array(definition: Definition) -> Union[Base, bool, str, float, list]:
    deconstruct = definition.type.split(":")
    inner_interval = ':'.join(deconstruct[2:])

    value = rand.array(
        _type=deconstruct[1],
        inner_interval=inner_interval,
        interval=definition.interval
    )

    return base(definition.name, value)


def obj(definition: Definition) -> Base:
    def inner(definition: Definition, node: Base):
        for m in definition.model:
            if m.type == "object":
                inner_base = Base()
                if m.name:
                    inner_base.__setattr__(m.name, Base())
                    inner_base = inner_base.__getattribute__(m.name)
                inner(m, inner_base)
                node.__setattr__(m.name, inner_base)
            else:
                value = switch(m)
                value = value.__getattribute__(m.name)
                node.__setattr__(m.name, value)

    root = Base()
    named_root = None
    if definition.name:
        root.__setattr__(definition.name, Base())
        named_root = root.__getattribute__(definition.name)

    if named_root:
        inner(definition, named_root)
    else:
        inner(definition, root)
    return root


def switch(definition: Definition) -> Union[Base, bool, str, list, float]:
    t = definition.type.split(":")[0]
    return {
        "boolean": boolean,
        "number": number,
        "string": string,
        "array": array,
        "object": obj
    }.get(t)(definition)


def create_data(definition: Definition) -> Callable:
    def create_data_wrapper():
        return switch(definition)
    return create_data_wrapper
