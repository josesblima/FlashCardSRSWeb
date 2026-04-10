import pytest

from flashcardsrsweb.cards.domain import Flashcard
from flashcardsrsweb.db.uow import UnitOfWork

@pytest.fixture
async def persisted_card():
    card = Flashcard(
            front_title="Front of the Flashcard",
            front_description="Front Description",
            back_description="Back Description"
            )

    async with UnitOfWork() as uow:
        persisted = await uow.cards.save(card=card)
    yield persisted
    assert 0 == 0
