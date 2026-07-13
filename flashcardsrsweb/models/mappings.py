from sqlalchemy.orm import properties, relationship
from flashcardsrsweb.models.registry import mapper_registry
from flashcardsrsweb.cards.domain import Flashcard
from flashcardsrsweb.models.flashcard import flashcards_table
from flashcardsrsweb.models.user import users_table
from flashcardsrsweb.users.domain import User

mapper_registry.map_imperatively(
    Flashcard,
    flashcards_table,
    properties={
        'user': relationship(
            'User',
            primaryjoin='and_(Flashcard.user_id == User.id)',
            lazy='noload',
            ),
        }
)

mapper_registry.map_imperatively(
    User,
    users_table,
    properties={}
    )
