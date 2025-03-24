from http import HTTPStatus
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from flashcardsrsweb.cards.create import CreateCardUseCase
from flashcardsrsweb.cards.dto import CreateCardDTO
from flashcardsrsweb.cards.read import ReadCardUseCase, ReadListCardUseCase
from flashcardsrsweb.utils.json_response import JsonResponse

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
    return JsonResponse.obj_to_json(result)

@router.post(
    '/{card_id}',
    name='Get Card',
)
async def get(
        card_id: int
):
    result = await ReadCardUseCase().execute(card_id=card_id)
    return JsonResponse.obj_to_json(result)

@router.get(
    '',
    name='List Cards',
)
async def list():
    result = await ReadListCardUseCase().execute()
    return JsonResponse.obj_to_json(result)
