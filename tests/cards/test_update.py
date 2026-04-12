import pytest

from flashcardsrsweb.cards.update import UpdateCardUseCase
from flashcardsrsweb.cards.dto import UpdateCardDTO
from flashcardsrsweb.cards.domain import Flashcard

pytestmark = pytest.mark.asyncio

class TestUpdateCardUseCase():
    @pytest.mark.asyncio
    async def test_when_called_usecase_should_return_create_dto(
        self, persisted_card: Flashcard):
        persisted = persisted_card
        use_case = UpdateCardUseCase()
        dto: UpdateCardDTO = UpdateCardDTO(
            id = persisted.id,  # type: ignore
            front_title = "new_title",
            front_description = "new_front_desc",
            back_description = "new_back_desc"
            )
        result = await use_case.execute(dto=dto)
 
        assert isinstance(result, Flashcard)
        assert result.front_title == dto.front_title
        assert result.back_description == dto.back_description
