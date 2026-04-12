from pydantic import BaseModel


def update_values(entity, dto: BaseModel):
    values = dto.model_dump()
    for key, value in values.items():
        setattr(entity, key, value)
    return entity

