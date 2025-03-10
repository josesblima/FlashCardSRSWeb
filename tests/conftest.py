# tests/conftest.py
import pytest
import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

# Import Base from the new location
from flashcardsrsweb.db.base import Base

# Import your mappings to ensure they're registered
import flashcardsrsweb.models.mappings
from flashcardsrsweb.cards.domain import Flashcard

# Load environment variables
load_dotenv()

# Constants for test database
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL", "postgresql://flashcards_user:my_password@localhost/flashcards_test_db")
TEST_ASYNC_DATABASE_URL = TEST_DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

# Async fixtures for tests
@pytest.fixture(scope="session")
async def async_test_engine():
    """Create a test async engine for the whole test session."""
    engine = create_async_engine(TEST_ASYNC_DATABASE_URL)
    yield engine
    # Cleanup after all tests
    await engine.dispose()

@pytest.fixture(scope="function")
async def async_test_db(async_test_engine):
    """Create all tables before test and drop them after."""
    # Create all tables
    async with async_test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # Run tests
    yield
    
    # Drop all tables after test
    async with async_test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture(scope="function")
async def db_session(async_test_engine, async_test_db):
    """Create a new test database session for each test."""
    # Create a new session for a test
    async with async_test_engine.connect() as connection:
        await connection.begin()
        session = AsyncSession(bind=connection, expire_on_commit=False)
        
        yield session
        
        # Close session and rollback transaction after test
        await session.close()
        await connection.rollback()
