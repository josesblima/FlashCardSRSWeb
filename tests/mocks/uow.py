# tests/mocks/uow.py
from typing import Self
from unittest.mock import AsyncMock

class MockUnitOfWork:
    """Mock implementation of UnitOfWork for testing."""
    
    def __init__(self):
        # Create a mock repository with a save method
        self.cards = AsyncMock()
        self.cards.save = AsyncMock()
        
        # Track context management
        self.entered = False
        self.exited = False
        self.committed = False
        self.rolled_back = False
    
    async def __aenter__(self) -> Self:
        self.entered = True
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.exited = True
        if exc_type:
            self.rolled_back = True
            return False
        self.committed = True
        return True
