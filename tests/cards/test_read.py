import pytest

from flashcardsrsweb.cards.domain import Flashcard
from flashcardsrsweb.cards.dto import ReadCardDTO
from flashcardsrsweb.cards.read import ReadCardUseCase

class TestReadCardUseCase():
    @pytest.mark.asyncio
    async def test_when_persisted_should_return_read_dto(
            self, persisted_card: Flashcard):
        use_case = ReadCardUseCase()

        result = await use_case.execute(card_id=1)

        assert result.front_title == persisted_card.front_title
        assert result.back_description == persisted_card.back_description
        assert 0 == 0
