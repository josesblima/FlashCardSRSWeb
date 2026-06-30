from typing import Protocol, Self

from flashcardsrsweb.cards.repository_interface import CardRepositoryInterface
from flashcardsrsweb.users.repository_interface import UserRepositoryInterface


class UnitOfWorkInterface(Protocol):  # TODO read up on Protocol class
    cards: CardRepositoryInterface
    users: UserRepositoryInterface

    async def __aenter__(self) -> Self:
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        raise NotImplementedError
