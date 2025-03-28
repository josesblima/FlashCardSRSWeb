# tests/conftest.py
import pytest
import os
import inject
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

# Import models and mappings
from flashcardsrsweb.db.base import Base
import flashcardsrsweb.models.mappings
from flashcardsrsweb.cards.domain import Flashcard
from flashcardsrsweb.db.uow_interface import UnitOfWorkInterface
from tests.mocks.uow import MockUnitOfWork

# Load environment variables
load_dotenv()

# Constants for test database
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL", "postgresql://flashcards_user:my_password@localhost/flashcards_test_db")
TEST_ASYNC_DATABASE_URL = TEST_DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

# Configure dependency injection for tests
@pytest.fixture(autouse=True)
def setup_test_inject():
    """Configure inject with test dependencies."""
    # Store the original configuration key to restore after test
    try:
        inject.get_injector()
        was_configured = True
    except inject.InjectorException:
        was_configured = False
    
    # Configure with test dependencies
    def config(binder: inject.Binder):
        binder.bind_to_provider(UnitOfWorkInterface, lambda: MockUnitOfWork())
    
    inject.clear_and_configure(config)
    
    yield
    
    # Clean up to avoid affecting other tests
    inject.clear()
    
    # Restore original configuration if it existed
    if was_configured:
        from flashcardsrsweb.inject import configure_inject
        configure_inject()

# SQLAlchemy test fixtures
@pytest.fixture
async def async_test_engine():
    """Create a test async engine for each test."""
    engine = create_async_engine(TEST_ASYNC_DATABASE_URL)
    yield engine
    # Cleanup after test
    await engine.dispose()

@pytest.fixture
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

@pytest.fixture
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
