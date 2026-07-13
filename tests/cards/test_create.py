import pytest

from flashcardsrsweb.cards.create import CreateCardUseCase
from flashcardsrsweb.cards.dto import CreateCardDTO
from flashcardsrsweb.cards.domain import Flashcard
from flashcardsrsweb.users.domain import User
from flashcardsrsweb.utils.not_none import assert_not_none

class TestCreateCardUseCase():
    async def test_when_called_usecase_should_return_create_dto(
        self, persisted_user: User
    ):
        use_case = CreateCardUseCase()
        dto: CreateCardDTO = CreateCardDTO(
            user_id = assert_not_none(persisted_user.id),
            front_title = "title",
            front_description = "front_desc",
            back_description = "back_desc"
            )
        result = await use_case.execute(dto=dto)
 
        assert isinstance(result, Flashcard)
        assert result.user_id == persisted_user.id
