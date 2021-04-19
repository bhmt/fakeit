from pydantic import validator
from typing import Union, List
from .base import Base

base_types = ("boolean", "number", "string", "object")


def __validate_array_type__(v: str) -> (str, bool):
    deconstruct = v.split(":")
    msg = []

    if len(deconstruct) == 1:
        msg.append("array must have a defined inner type")
    elif deconstruct[1] not in base_types:
        msg.append(f"argument type value '{v}' is not allowed in array")

    if len(deconstruct) > 2:
        try:
            int(deconstruct[2])
        except ValueError:
            msg.append(f"inner interval value '{deconstruct[2]}' not allowed")
        try:
            int(deconstruct[3])
        except IndexError:
            pass
        except ValueError:
            msg.append(f"inner interval value '{deconstruct[3]}' not allowed")

    if msg:
        return ('\n'.join(msg), False)
    return ("", True)


def __validate_interval_as_string__(v: str) -> (str, bool):
    msg = []
    deconstruct = v.split(":")

    if deconstruct[0] == "":
        try:
            int(deconstruct[1])
        except IndexError:
            msg.append("must have upper limit")
        except ValueError:
            msg.append(f"interval value '{deconstruct[1]}' not allowed")
    else:
        try:
            _ = int(deconstruct[0])
        except ValueError:
            msg.append(f"interval value '{deconstruct[0]}' not allowed")
        try:
            int(deconstruct[1])
        except IndexError:
            pass
        except ValueError:
            if deconstruct[1]:
                msg.append(f"interval value '{deconstruct[1]}' not allowed")
            else:
                msg.append("must have upper limit")

    if msg:
        return ("\n".join(msg), False)
    return ("", True)


class Definition(Base):
    type: str
    name: str = None
    interval: Union[str, int] = None
    model: List['Definition'] = None

    @validator('type')
    def allowed_types(cls, v: str):
        v = v.lower()
        if v.startswith("array"):
            msg, success = __validate_array_type__(v)
            if success is False:
                raise ValueError(msg)
        elif v.lower() not in base_types:
            raise ValueError(f"argument type value '{v}' is not allowed")

        return v

    @validator('interval')
    def allowed_interval(cls, v: Union[str, int]):
        if v is None or isinstance(v, int):
            return v
        msg, success = __validate_interval_as_string__(v)
        if success is False:
            raise ValueError(msg)

        return v


Definition.update_forward_refs()
