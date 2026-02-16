"""Database initialization."""

from .database import engine, Base
from .models import GameServer  # Import all models


def initialize_database():
    """Create all database tables defined in models."""
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully")


if __name__ == "__main__":
    initialize_database()
