import inject

from flashcardsrsweb.cards.domain import Flashcard
from flashcardsrsweb.cards.dto import CreateCardDTO
from flashcardsrsweb.db.uow import UnitOfWork

class CreateCardUseCase():
    async def execute(self, *, dto: CreateCardDTO) -> Flashcard:
        card = Flashcard(
            front_title=dto.front_title,
            front_description=dto.front_description,
            back_description=dto.back_description
        )
        async with UnitOfWork() as uow:
            result: Flashcard = await uow.cards.save(card=card)
        return result
