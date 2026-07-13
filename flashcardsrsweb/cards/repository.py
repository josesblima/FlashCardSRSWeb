from flashcardsrsweb.cards.domain import Flashcard

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select

from flashcardsrsweb.cards.repository_interface import CardRepositoryNotFoundError

class CardRepositorySQLAlchemy:
    def __init__(self, *, session: AsyncSession):
        self._session = session

    async def save(self, *, card: Flashcard) -> Flashcard:
        self._session.add(card)
        await self._session.flush()
        return card

    async def get(self, *, card_id: int) -> Flashcard:
        statement = (
            select(Flashcard)
            .where(Flashcard.id == card_id)  # type: ignore
        )
        if not (card := await self._session.scalar(statement)):
            raise CardRepositoryNotFoundError # Catch this with CardNotFoundError in the usecase
        return card  # type: ignore
        
    async def list(self):
        statement = (
            select(Flashcard)
        )

        result = await self._session.scalars(statement)
        return result.unique().all()

    async def delete(self, *, card_id: int) -> None:
        statement = (
            delete(Flashcard)
            .where(Flashcard.id == card_id)  # type: ignore
            )
        await self._session.execute(statement)

