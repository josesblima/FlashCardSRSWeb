import pytest

from flashcardsrsweb.db.uow import UnitOfWork
from flashcardsrsweb.users.domain import User
@pytest.fixture
async def persisted_user():
    user = User(
            oauth_provider = 'Google',
            oauth_provider_id = 'asdfasdf',
            email = 'asdf@asdf.com',
            display_name = 'asdf'
            )

    async with UnitOfWork() as uow:
        persisted = await uow.users.save(user=user)
    yield persisted
