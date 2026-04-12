import pytest
import inject
from dotenv import load_dotenv
from sqlalchemy import text

from flashcardsrsweb.db.uow import UnitOfWork
from flashcardsrsweb.db.uow_interface import UnitOfWorkInterface

# SQLAlchemy needs these imports here so it knows the mappings between objects and tables
import flashcardsrsweb.models.mappings

load_dotenv('.env.test', override=True)


# Scope configures it for the whole test running session
# Autouse makes it so that Pytest calls it once at the start of the tests
@pytest.fixture(scope='session', autouse=True)
def _inject_config():
    def config(binder: inject.Binder) -> None:
        binder.bind_to_provider(UnitOfWorkInterface, lambda: UnitOfWork())
    inject.clear_and_configure(config)

@pytest.fixture(autouse=True)
async def clean_db():
    yield
    async with UnitOfWork() as uow:
        await uow._session.execute(text("TRUNCATE TABLE flashcards RESTART IDENTITY CASCADE"))

@pytest.fixture()
def uow() -> UnitOfWorkInterface:
    @inject.autoparams()
    def _uow(uow: UnitOfWorkInterface) -> UnitOfWorkInterface:
        return uow
    return _uow()
