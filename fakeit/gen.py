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


def obj(definition: Definition) -> Dummy:
    def inner(definition: Definition, node: Dummy):
        for m in definition.model:
            if m.type == "object":
                dummy = Dummy()
                if m.name:
                    dummy.__setattr__(m.name, Dummy())
                    dummy = dummy.__getattribute__(m.name)
                inner(m, dummy)
                node.__setattr__(m.name, dummy)
            else:
                value = switch(m)
                value = value.__getattribute__(m.name)
                node.__setattr__(m.name, value)

    root = Dummy()
    named_root = None
    if definition.name:
        root.__setattr__(definition.name, Dummy())
        named_root = root.__getattribute__(definition.name)

    if named_root:
        inner(definition, named_root)
    else:
        inner(definition, root)
    return root


def switch(definition: Definition) -> Union[Dummy, bool, str, list, float]:
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
