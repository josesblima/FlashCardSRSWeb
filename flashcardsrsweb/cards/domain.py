from dataclasses import dataclass

@dataclass(kw_only=True)
class Flashcard():
    id: int | None = None
    front_title: str
    front_description: str
    back_description: str
