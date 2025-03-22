# tests/mocks/uow.py
from typing import Self
from unittest.mock import AsyncMock

from flashcardsrsweb.cards.domain import Flashcard

class MockUnitOfWork:
    """Mock implementation of UnitOfWork for testing."""
    
    def __init__(self):
        # Create a mock repository with a save method
        self.cards = AsyncMock()
        
        # Configure the save method to return a proper Flashcard instance
        async def mock_save(card: Flashcard) -> Flashcard:
            # This returns the same card object but with an ID set
            # (simulating what the database would do)
            card.id = 1  # Set a mock ID
            return card
            
        self.cards.save = mock_save
        
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
