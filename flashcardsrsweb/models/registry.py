from sqlalchemy import MetaData
from sqlalchemy.orm import registry

# This whole thing is because of Alembic's downgrades. Whenever you create a constraint, PostgreSQL has a particular naming convention for it. The issue is when you create Alembic's migration file, it can create the constraint without naming it, no problem, but then, on the downgrade it can't delete it because it was PostgreSQL who ended up naming it. So I had two options, manually naming each constraint in the migration file so I could call the constraint on the downgrade or creating this naming convention, this way there's this default way to name things, and constraints are named by SQLAlchmy as opposed to by PostgreSQL.
naming_convention = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
        }

mapper_registry = registry(metadata=MetaData(naming_convention=naming_convention))

