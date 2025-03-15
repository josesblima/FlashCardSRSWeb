# flashcardsrsweb/__init__.py
"""
FlashCardSRSWeb - High customizability and low friction system to memorize anything!
"""

from inject import Binder
from flashcardsrsweb.inject import uow_config

# Initialize dependency injection when the package is imported
uow_config()
