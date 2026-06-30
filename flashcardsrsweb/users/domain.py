from dataclasses import dataclass

@dataclass(kw_only=True)
class User():
    id: int | None = None
    oauth_provider: str
    oauth_provider_id: str
    email: str
    display_name: str
