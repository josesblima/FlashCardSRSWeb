# flashcardsrsweb/__init__.py
"""
FlashCardSRSWeb - High customizability and low friction system to memorize anything!
"""

from flashcardsrsweb.inject import configure_inject

# Initialize dependency injection when the package is imported
configure_inject()
