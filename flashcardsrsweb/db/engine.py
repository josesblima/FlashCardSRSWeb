# flashcardsrsweb/db/engine.py
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.pool import NullPool
import os

class EngineManager:
    _engine: AsyncEngine = None

    @classmethod
    def get_engine(cls) -> AsyncEngine:
        if cls._engine is None:
            database_url = os.getenv("DATABASE_URL")
            async_db_url = database_url.replace("postgresql://", "postgresql+asyncpg://")
            if os.getenv("TESTING"):
                cls._engine = create_async_engine(async_db_url, poolclass=NullPool)
            else:
                cls._engine = create_async_engine(
                    async_db_url,
                    pool_pre_ping=True,
                    pool_size=5,
                    pool_timeout=30,
                    max_overflow=10
                )
        return cls._engine
