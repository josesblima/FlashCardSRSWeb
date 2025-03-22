import inject
from flashcardsrsweb.db.uow import UnitOfWork
from flashcardsrsweb.db.uow_interface import UnitOfWorkInterface

def uow_config(binder: inject.Binder):
    binder.bind_to_provider(UnitOfWorkInterface, lambda: UnitOfWork())

def configure_inject():
    inject.configure(uow_config)
