import inject

from flashcardsrsweb.db.uow import UnitOfWork
from flashcardsrsweb.db.uow_interface import UnitOfWorkInterface

def configure_inject():
    def config(binder: inject.Binder):
        binder.bind_to_provider(UnitOfWorkInterface, lambda: UnitOfWork())

    inject.clear_and_configure(config)
