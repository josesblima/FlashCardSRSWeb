# flashcardsrsweb/db/uow.py
from typing import Self
from sqlalchemy.ext.asyncio import AsyncSession

from flashcardsrsweb.db.session import SessionManager
from flashcardsrsweb.cards.repository import CardRepositorySQLAlchemy

class UnitOfWork:
    _session: AsyncSession
    cards: CardRepositorySQLAlchemy

    async def __aenter__(self) -> Self:
        self._session = await SessionManager.get_session()
        self._initialize_repositories()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            await self._session.rollback()
            await self._session.close()
            raise exc_val

        await self._session.commit()
        await self._session.close()

    def _initialize_repositories(self):
        self.cards = CardRepositorySQLAlchemy(session=self._session)
