from pydantic import BaseModel


class NameIdPair(BaseModel):
    id: int
    name: str


class GenericResponse(BaseModel):
    code: int
    type: str
    message: str


class Pet(BaseModel):
    id: int
    category: NameIdPair
    name: str
    photoUrls: list[str]
    tags: list[NameIdPair]
    status: str
