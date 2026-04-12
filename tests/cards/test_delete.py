import pytest

from flashcardsrsweb.cards.delete import DeleteCardUseCase
from flashcardsrsweb.cards.domain import Flashcard
from flashcardsrsweb.db.uow_interface import UnitOfWorkInterface

class TestDeleteCardUseCase():
    @pytest.mark.asyncio
    async def test_when_persisted_should_delete(
            self, persisted_card: Flashcard, uow: UnitOfWorkInterface):
        card_id = persisted_card.id
        use_case = DeleteCardUseCase()

        await use_case.execute(card_id=card_id)

        async with uow:
            deleted_card = await uow.cards.get(card_id=card_id)
        assert deleted_card is None
