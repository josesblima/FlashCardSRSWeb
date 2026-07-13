import pytest

from flashcardsrsweb.cards.delete import DeleteCardUseCase
from flashcardsrsweb.cards.domain import Flashcard
from flashcardsrsweb.cards.repository_interface import CardRepositoryNotFoundError
from flashcardsrsweb.db.uow_interface import UnitOfWorkInterface
from flashcardsrsweb.users.domain import User
from flashcardsrsweb.utils.not_none import assert_not_none

class TestDeleteCardUseCase():
    @pytest.mark.asyncio
    async def test_when_persisted_should_delete(
            self, persisted_card: tuple[Flashcard, User], uow: UnitOfWorkInterface):
        card_id = persisted_card[0].id
        use_case = DeleteCardUseCase()

        await use_case.execute(card_id=assert_not_none(card_id))

        async with uow:
            with pytest.raises(CardRepositoryNotFoundError):
                await uow.cards.get(card_id=assert_not_none(card_id))

