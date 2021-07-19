from pydantic import BaseModel


class PokeTypeBase(BaseModel):

    name: str
    description: str


class PokeTypeIn(PokeTypeBase):
    pass


class PokeTypeOut(PokeTypeBase):
    id: int
