from sqlalchemy.orm import relationship
from flashcardsrsweb.models.registry import mapper_registry
from flashcardsrsweb.cards.domain import Flashcard
from flashcardsrsweb.models.flashcard import flashcards_table

mapper_registry.map_imperatively(
    Flashcard,
    flashcards_table,
    properties={}
)
