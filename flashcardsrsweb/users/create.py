import inject

from flashcardsrsweb.db.uow_interface import UnitOfWorkInterface
from flashcardsrsweb.users.domain import User
from flashcardsrsweb.users.dto import CreateUserDTO
from flashcardsrsweb.users.exceptions import UserAlreadyExistsError
from flashcardsrsweb.users.messages import UserUseCaseMessages

class CreateUserUseCase():
    @inject.autoparams()
    def __init__(self, *, uow: UnitOfWorkInterface):
        self._uow = uow

    async def execute(self, *, dto: CreateUserDTO) -> User:
        async with self._uow as uow:
            if await uow.users.get_by_email(user_email=dto.email) is not None:
                raise UserAlreadyExistsError(UserUseCaseMessages.ALREADY_EXISTS_ERROR)
            user = User(
                oauth_provider = dto.oauth_provider,
                oauth_provider_id = dto.oauth_provider_id,
                email = dto.email,
                display_name = dto.display_name
           )
            result: User = await uow.users.save(user=user)
        return result
