from pydantic import BaseModel


class Dummy(BaseModel):
    class Config:
        orm_mode = True
        extra = 'allow'
