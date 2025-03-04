import pytest

from flashcardsrsweb.cards.create import CreateCardUseCase
from flashcardsrsweb.cards.dto import CreateCardDTO

pytestmark = pytest.mark.asyncio

class TestCreateCardUseCase():
    @pytest.mark.asyncio
    async def test_when_called_usecase_should_return_create_dto(self):
        use_case = CreateCardUseCase()
        dto: CreateCardDTO = CreateCardDTO(
            front_title = "title",
            front_description = "front_desc",
            back_description = "back_desc"
            )
        result = await use_case.execute(dto=dto)
        assert result == dto
