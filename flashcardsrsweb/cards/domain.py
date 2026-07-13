from dataclasses import dataclass, field

from flashcardsrsweb.users.domain import User

@dataclass(kw_only=True)
class Flashcard():
    id: int | None = None
    user_id: int
    front_title: str
    front_description: str
    back_description: str
    user: User = field(init=False)

