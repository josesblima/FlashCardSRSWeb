import pytest

from flashcardsrsweb.cards.update import UpdateCardUseCase
from flashcardsrsweb.cards.dto import UpdateCardDTO
from flashcardsrsweb.cards.domain import Flashcard
from flashcardsrsweb.users.domain import User
from flashcardsrsweb.utils.not_none import assert_not_none

class TestUpdateCardUseCase():
    @pytest.mark.asyncio
    async def test_when_called_usecase_should_return_create_dto(
        self, persisted_card: tuple[Flashcard, User]):
        card = persisted_card[0]
        use_case = UpdateCardUseCase()
        dto: UpdateCardDTO = UpdateCardDTO(
            id = assert_not_none(card.id),
            front_title = "new_title",
            front_description = "new_front_desc",
            back_description = "new_back_desc"
            )
        result = await use_case.execute(dto=dto)
 
        assert isinstance(result, Flashcard)
        assert result.front_title == dto.front_title
        assert result.back_description == dto.back_description
