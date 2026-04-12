import inject

from flashcardsrsweb.cards.domain import Flashcard
from flashcardsrsweb.cards.dto import UpdateCardDTO
from flashcardsrsweb.db.uow_interface import UnitOfWorkInterface
from flashcardsrsweb.utils.update_values import update_values


class UpdateCardUseCase():
    @inject.autoparams()
    def __init__(self, *, uow: UnitOfWorkInterface):
        self._uow = uow

    async def execute(self, *, dto: UpdateCardDTO) -> Flashcard | None:
        try:
            async with self._uow as uow:
                old_card = await uow.cards.get(card_id=dto.id)
                card = update_values(old_card, dto)
                result: Flashcard = await uow.cards.save(card=card)
                return result
            
        except:
            print("Error Implement Later")
