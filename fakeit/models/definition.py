from pydantic import BaseModel, validator
from typing import Union, Callable, List
from enum import Enum

base_types = ("boolean", "number", "string", "object")


def __validate_array_type__(v: str) -> (str, bool):
    deconstruct = v.split(":")
    msg = []
    if deconstruct[1] not in base_types:
        msg.append(f"argument type value '{v}' is not allowed in array.")
    if len(deconstruct) > 2:
        try:
            int(deconstruct[2])
        except ValueError:
            msg.append(f"inner interval value '{deconstruct[2]}' not allowed.")
        try:
            int(deconstruct[3])
        except IndexError:
            pass
        except ValueError:
            msg.append(f"inner interval value '{deconstruct[3]}' not allowed.")

    if msg:
        return ('\n'.join(msg), False)
    return ("", True)


class Definition(BaseModel):
    type: str
    name: str = None
    interval: Union[str, int] = None
    model: List['Definition'] = None

    @validator('type')
    def allowed_types(cls, v: str):
        if v.lower().startswith("array:"):
            msg, success = __validate_array_type__(v)
            if success is False:
                raise ValueError(msg)
            return v
        if v.lower() not in base_types:
            raise ValueError(f"argument type value '{v}' is not allowed.")

        return v

    class Config:
        orm_mode = True
        extra = 'allow'


Definition.update_forward_refs()
