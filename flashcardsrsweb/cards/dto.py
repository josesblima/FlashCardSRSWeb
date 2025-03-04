from dataclasses import dataclass

@dataclass
class CreateCardDTO():
    front_title: str
    front_description: str
    back_description: str
