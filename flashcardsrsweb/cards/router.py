from http import HTTPStatus
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from flashcardsrsweb.cards.create import CreateCardUseCase
from flashcardsrsweb.cards.dto import CreateCardDTO

router = APIRouter(
    prefix="/cards",
    tags=["cards"]
)

@router.post(
    '',
    name='Create Card',
    status_code=HTTPStatus.CREATED,
    # responses=Response.HTTP_400_BAD_REQUEST
)
async def create(
        dto: CreateCardDTO,
):
    result = await CreateCardUseCase().execute(dto=dto)
    return json_response(result)
