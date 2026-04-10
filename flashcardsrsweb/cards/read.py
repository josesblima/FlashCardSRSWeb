import inject
from automapper import mapper

from flashcardsrsweb.cards.domain import Flashcard
from flashcardsrsweb.cards.dto import ReadCardDTO, ReadCardListDTO
from flashcardsrsweb.db.uow_interface import UnitOfWorkInterface

class ReadCardUseCase():
    @inject.autoparams()
    def __init__(self, *, uow: UnitOfWorkInterface):
        self._uow = uow

    async def execute(self, *, card_id: int) -> ReadCardDTO:
        async with self._uow as uow:
            result: Flashcard = await uow.cards.get(card_id=card_id)
            print(result)
        return mapper.to(ReadCardDTO).map(result)

class ReadListCardUseCase():
    @inject.autoparams()
    def __init__(self, *, uow: UnitOfWorkInterface):
        self._uow = uow

    async def execute(self) -> list[ReadCardListDTO]:
        async with self._uow as uow:
            result = await uow.cards.list()
        cards = [mapper.to(ReadCardListDTO).map(card) for card in result]
        print(result)
        return result
        
