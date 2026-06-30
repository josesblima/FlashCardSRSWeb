from sqlalchemy import Table, Integer, Column, Text, UniqueConstraint
from .registry import mapper_registry

users_table = Table(
    'users',
    mapper_registry.metadata,
    Column('id', Integer(), primary_key=True, autoincrement=True, index=True),
    Column('oauth_provider', Text(), nullable=False),
    Column('oauth_provider_id', Text(), nullable=False),
    Column('email', Text(), nullable=False, unique=True),
    Column('display_name', Text(), nullable=False),
    UniqueConstraint('oauth_provider', 'oauth_provider_id') # This allows the existence of a microsoft and google oauth_provider_id that are the same
    )
