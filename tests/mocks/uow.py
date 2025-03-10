# tests/mocks/uow.py
from unittest.mock import AsyncMock, MagicMock
from typing import Optional
from flashcardsrsweb.db.uow import UnitOfWork

class MockUnitOfWork(UnitOfWork):
    """
    A mock implementation of UnitOfWork for testing.
    This allows tests to run without a real database connection.
    """
    
    def __init__(self):
        self.cards = AsyncMock()
        self.committed = False
        self.rolled_back = False
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
            return False
        await self.commit()
        return True
    
    async def commit(self):
        self.committed = True
    
    async def rollback(self):
        self.rolled_back = True
