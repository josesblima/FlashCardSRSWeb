from sqlalchemy.ext.asyncio import AsyncSession

from flashcardsrsweb.cards.repository import CardRepositorySQLAlchemy

class UnitOfWork:
    _session: AsyncSession

    flashcards: CardRepositorySQLAlchemy

    async def __aenter__(self) -> Self:
        self._session = await SessionManager
