from flashcardsrsweb.cards.dto import CreateCardDTO
class CreateCardUseCase():
    async def execute(self, dto: CreateCardDTO) -> CreateCardDTO:
        return dto
