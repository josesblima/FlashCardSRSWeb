import pytest

from flashcardsrsweb.users.create import CreateUserUseCase
from flashcardsrsweb.users.domain import User
from flashcardsrsweb.users.dto import CreateUserDTO
from flashcardsrsweb.users.exceptions import UserAlreadyExistsError
from flashcardsrsweb.users.messages import UserUseCaseMessages

pytestmark = pytest.mark.asyncio

class TestCreateUserUseCase():
    @pytest.mark.asyncio
    async def test_when_valid_dto_should_persist(self):
        dto = CreateUserDTO(
            oauth_provider = 'Google',
            oauth_provider_id = 'asdfasdf',
            email = 'asdf@asdf.com',
            display_name = 'asdf'
        )
        use_case = CreateUserUseCase()

        result = await use_case.execute(dto=dto)
        assert result is not None
        assert dto.display_name == result.display_name

    async def test_when_email_already_exists_should_raise_error(
            self, persisted_user: User):
        dto = CreateUserDTO(
            oauth_provider = 'Google',
            oauth_provider_id = 'asdfasdf',
            email = persisted_user.email,
            display_name = 'asdf'
        )
        use_case = CreateUserUseCase()
        
        with pytest.raises(UserAlreadyExistsError) as e:
            await use_case.execute(dto=dto)

        assert str(e.value) == UserUseCaseMessages.ALREADY_EXISTS_ERROR


