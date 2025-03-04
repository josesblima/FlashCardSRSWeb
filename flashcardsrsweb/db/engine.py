# flashcardsrsweb/db/engine.py
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
import os
from dotenv import load_dotenv

load_dotenv()

class EngineManager:
    _engine: AsyncEngine = None

    @classmethod
    def get_engine(cls) -> AsyncEngine:
        if cls._engine is None:
            database_url = os.getenv("DATABASE_URL")
            async_db_url = database_url.replace("postgresql://", "postgresql+asyncpg://")
            cls._engine = create_async_engine(
                async_db_url,
                pool_pre_ping=True,
                pool_size=5,
                pool_timeout=30,
                max_overflow=10
            )
        return cls._engine
