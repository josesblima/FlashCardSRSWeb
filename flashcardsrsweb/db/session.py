# flashcardsrsweb/db/session.py
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from flashcardsrsweb.db.engine import EngineManager
from flashcardsrsweb.db.base import Base

class SessionManager:
    @staticmethod
    async def get_session() -> AsyncSession:
        async_session = async_sessionmaker(
            bind=EngineManager.get_engine(),
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False
        )
        async with async_session() as session:
            return session
