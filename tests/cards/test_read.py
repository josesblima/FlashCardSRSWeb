import pytest

from flashcardsrsweb.cards.domain import Flashcard
from flashcardsrsweb.cards.dto import ReadCardDTO
from flashcardsrsweb.cards.read import ReadCardUseCase
from flashcardsrsweb.users.domain import User
from flashcardsrsweb.utils.not_none import assert_not_none

class TestReadCardUseCase():
    @pytest.mark.asyncio
    async def test_when_persisted_should_return_read_dto(
            self, persisted_card: tuple[Flashcard, User]):
        card = persisted_card[0]
        use_case = ReadCardUseCase()

        result = await use_case.execute(card_id=assert_not_none(card.id))

        assert result.front_title == card.front_title
        assert result.back_description == card.back_description
        assert 0 == 0
