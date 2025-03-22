import inject

class Binder:
    def config(self, binder: inject.Binder):
        binder.install(self._uow)

    def _uow(self, binder:inject.Binder):
        from flashcardsrsweb.db.
