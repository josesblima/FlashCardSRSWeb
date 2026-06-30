from typing import Protocol

from flashcardsrsweb.users.domain import User


class UserRepositoryInterface(Protocol):
    async def save(self, *, user: User) -> User:
        raise NotImplementedError

    async def get(self, *, user_id: int) -> User:
        raise NotImplementedError

    # async def list(self) -> list[ReadUserListDTO]
    #     raise NotImplementedError

    async def get_by_email(self, *, user_email: str) -> User | None:
        raise NotImplementedError

    async def delete(self, *, user_id: int) -> None:
        raise NotImplementedError
