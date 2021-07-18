from pydantic import BaseModel


class PokeTypeBase(BaseModel):

    id: int
    name: str
    description: str
