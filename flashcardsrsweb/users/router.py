from http import HTTPStatus
from fastapi import APIRouter

from flashcardsrsweb.users.create import CreateUserUseCase
from flashcardsrsweb.users.dto import CreateUserDTO
from flashcardsrsweb.utils.json_response import JsonResponse

router = APIRouter(
        prefix="/users",
        tags=["users"]
        )

@router.post(
        '',
        name='Create User',
        status_code=HTTPStatus.CREATED,
        )
async def create(
        dto: CreateUserDTO,
        ):
    result = await CreateUserUseCase().execute(dto=dto)
    return JsonResponse.obj_to_json(result)
