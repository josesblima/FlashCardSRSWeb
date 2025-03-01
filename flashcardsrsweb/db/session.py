import os
from typing import Generator
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

load_dotenv()
# Get database URL from environment variables or use a default for local development
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://flashcards_user:password@localhost/flashcards_db")

engine = create_engine(
    DATABASE_URL,
    echo=True, # Set to False in prod
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db() -> Generator[Session, None, None]:
    """
    Dependency for FastAPI to get database session.
    Yields a database session and ensures proper closing after use.
    
    Usage in FastAPI:
        @app.get("/users/")
        def read_users(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
