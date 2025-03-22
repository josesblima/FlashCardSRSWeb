from typing import Protocol, Self

from flashcardsrsweb.cards.repository_interface import CardRepositoryInterface


class UnitOfWorkInterface(Protocol):  # TODO read up on Protocol class
    cards: CardRepositoryInterface

    async def __aenter__(self) -> Self:
        raise NotImplementedError
        
    async def __aexit__(self) -> Self:
        raise NotImplementedError
