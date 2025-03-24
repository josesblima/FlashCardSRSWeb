from typing import Protocol

from flashcardsrsweb.cards.domain import Flashcard
from flashcardsrsweb.cards.dto import CardReadListDTO

class CardRepositoryInterface(Protocol):
    async def save(self, * card: Flashcard) -> Flashcard:
        raise NotImplementedError
        
    async def get(self, * card_id: int) -> Flashcard:
        raise NotImplementedError
        
    async def list(self) -> list[CardReadListDTO]:
        raise NotImplementedError
