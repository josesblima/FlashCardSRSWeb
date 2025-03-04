from flashcardsrsweb.cards.domain import Flashcard

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from flashcardsrsweb.cards.dto import CreateCardDTO

class CardRepositorySQLAlchemy:
    def __init__(self, *, session: AsyncSession):
        self._session = session

    async def save(self, *, card: Flashcard) -> Flashcard:
        self._session.add(card)
        await self._session.flush()
        card = await self.get(card_id=card.id)
        return card

    async def get(self, *, card_id: int) -> Flashcard:
        statement = (
            select(Flashcard)
            .where(Flashcard.id == card_id)
        )
        card = await self.session.scalar(statement)
        # Raise error if not statement
        return card
        
