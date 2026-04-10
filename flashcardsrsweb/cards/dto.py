from dataclasses import dataclass

@dataclass
class CreateCardDTO():
    front_title: str
    front_description: str
    back_description: str

@dataclass
class ReadCardDTO():
    front_title: str
    front_description: str
    back_description: str
    
@dataclass
class ReadCardListDTO():
    front_title: str
    front_description: str
    back_description: str
