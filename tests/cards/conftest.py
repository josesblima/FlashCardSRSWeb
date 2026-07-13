from collections.abc import AsyncGenerator
import pytest

from flashcardsrsweb.cards.domain import Flashcard
from flashcardsrsweb.db.uow import UnitOfWork
from flashcardsrsweb.users.domain import User
from flashcardsrsweb.utils.not_none import assert_not_none

@pytest.fixture
async def persisted_user() -> AsyncGenerator[User]:
    user = User(
            oauth_provider = "GOOGLE",
            oauth_provider_id = "db97531",
            email = "user_email@gmail.com",
            display_name = "Alex Barron"
            )

    async with UnitOfWork() as uow:
        persisted = await uow.users.save(user=user)
    yield persisted

@pytest.fixture
async def persisted_card(persisted_user: User) -> AsyncGenerator[tuple[Flashcard, User]]:
    card = Flashcard(
            user_id=assert_not_none(persisted_user.id),
            front_title="Front of the Flashcard",
            front_description="Front Description",
            back_description="Back Description"
            )

    async with UnitOfWork() as uow:
        persisted = await uow.cards.save(card=card)
    yield persisted, persisted_user
