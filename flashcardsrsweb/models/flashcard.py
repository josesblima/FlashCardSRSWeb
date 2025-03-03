from sqlalchemy import Table, Integer, Column, Text
from .registry import mapper_registry
flashcards_table = Table(
    'flashcards',
    mapper_registry.metadata,
    Column('id', Integer(), primary_key=True, autoincrement=True, index=True),
    Column('front_title', Text(), nullable=False),
    Column('front_description', Text(), nullable=False),
    Column('back_description', Text(), nullable=False),
    )
