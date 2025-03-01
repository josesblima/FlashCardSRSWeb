# tests/test_db_connection.py
import pytest
from sqlalchemy.sql import text

def test_database_connection(db_session):
    # Execute a simple query
    result = db_session.execute(text("SELECT 1"))
    assert result.scalar() == 1

def test_session_fixture(db_session):
    # Test that our session fixture is working
    assert db_session is not None
    # Check if we can perform a simple operation
    result = db_session.execute(text("SELECT 1"))
    assert result.scalar() == 1
