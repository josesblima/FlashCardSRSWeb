from pydantic import BaseModel

class CreateUserDTO(BaseModel):
    oauth_provider: str
    oauth_provider_id: str
    email: str
    display_name: str
