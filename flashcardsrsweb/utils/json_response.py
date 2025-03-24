from dataclasses import asdict, is_dataclass
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


# The response DTOs have to be converted to a dictionary before JSONResponse(ing)
class JsonResponse():
    def obj_to_json(obj):
        if is_dataclass(obj):
            return JSONResponse(
                content=jsonable_encoder(
                    asdict(obj)
                )
            )
        if isinstance(obj, list):
            return [asdict(item) for item in obj]
