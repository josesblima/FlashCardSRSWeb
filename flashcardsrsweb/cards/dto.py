from dataclasses import dataclass

@dataclass
class CreateCardDTO():
    front_title: str
    front_description: str
    back_description: str

@dataclass
class CardReadDTO():
    front_title: str
    front_description: str
    back_description: str
    
@dataclass
class CardReadListDTO():
    front_title: str
    front_description: str
    back_description: str
