from pydantic import BaseModel


class CreateCardDTO(BaseModel):
    front_title: str
    front_description: str
    back_description: str


class UpdateCardDTO(BaseModel):
    id: int
    front_title: str
    front_description: str
    back_description: str


class ReadCardDTO(BaseModel):
    front_title: str
    front_description: str
    back_description: str


class ReadCardListDTO(BaseModel):
    front_title: str
    front_description: str
    back_description: str

