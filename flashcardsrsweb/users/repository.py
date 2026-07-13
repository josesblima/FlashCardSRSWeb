from sqlalchemy.ext.asyncio import AsyncSession

from flashcardsrsweb.users.domain import User
from sqlalchemy import select

class UserRepositorySQLAlchemy:
    def __init__(self, *, session: AsyncSession):
        self._session = session

    async def save(self, *, user: User) -> User:
        self._session.add(user)
        await self._session.flush()
        return user

    async def get(self, *, user_id: int) -> User:
        statement = (
            select(User)
            .where(User.id == user_id)  # type: ignore
        )
        user = await self._session.scalar(statement)
        # TODO Raise error
        return user  # type: ignore

    async def get_by_email(self, *, user_email: str) -> User | None:
        statement = (
            select(User)
            .where(User.email == user_email)  # type: ignore
        )
        result = await self._session.scalar(statement)
        return result
