import inject

from flashcardsrsweb.db.uow_interface import UnitOfWorkInterface

class DeleteCardUseCase():
    @inject.autoparams()
    def __init__(self, *, uow: UnitOfWorkInterface):
        self._uow = uow

    async def execute(self, *, card_id: int) -> None:
        try:
            async with self._uow as uow:
                await uow.cards.get(card_id=card_id)
                await uow.cards.delete(card_id=card_id)
        except:
            print("Implement Error Later")
