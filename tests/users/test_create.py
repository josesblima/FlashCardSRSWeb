import pytest

from flashcardsrsweb.users.create import CreateUserUseCase
from flashcardsrsweb.users.domain import User
from flashcardsrsweb.users.dto import CreateUserDTO
from flashcardsrsweb.users.exceptions import UserAlreadyExistsError

class TestCreateUserUseCase():
    create_dto = CreateUserDTO(
            oauth_provider = 'Google',
            oauth_provider_id = 'asdfasdf',
            email = 'asdf@asdf.com',
            display_name = 'asdf'
            )
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

    async def test_when_email_already_exists_should_raise_user_already_exists_error(
        self, persisted_user: User
    ):
        use_case = CreateUserUseCase()

        with pytest.raises(UserAlreadyExistsError) as e:
            await use_case.execute(dto=self.create_dto)

        assert e.value.email == persisted_user.email


