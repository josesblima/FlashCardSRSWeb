from typing import Protocol

from flashcardsrsweb.cards.domain import Flashcard

class CardRepositoryInterface(Protocol):
    async def save(self, * card: Flashcard) -> Flashcard:
        raise NotImplementedError
        
    async def get(self, * card_id: Flashcard) -> Flashcard:
        raise NotImplementedError
