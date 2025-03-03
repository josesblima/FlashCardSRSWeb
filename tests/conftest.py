# tests/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flashcardsrsweb.db.session import Base, get_db

TEST_DATABASE_URL = "postgresql://flashcards_user:my_password@localhost/flashcards_test_db"

@pytest.fixture(scope="session")
def test_engine():
    engine = create_engine(TEST_DATABASE_URL)
    yield engine
    # Cleanup after all tests
    engine.dispose()

@pytest.fixture(scope="function")
def test_db(test_engine):
    # Create all tables
    Base.metadata.create_all(bind=test_engine)
    # Run tests
    yield
    # Drop all tables after test
    Base.metadata.drop_all(bind=test_engine)

@pytest.fixture(scope="function")
def db_session(test_engine, test_db):
    # Create a new session for a test
    connection = test_engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()
    
    yield session
    
    # Close session and rollback transaction after test
    session.close()
    transaction.rollback()
    connection.close()
