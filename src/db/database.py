from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from pathlib import Path

# Database path
DATABASE_URL = "sqlite:///./gamed.db"

# Create engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False,
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db_session():
    """Get a database session."""
    return SessionLocal()


def close_db_session(session):
    """Close a database session."""
    if session:
        session.close()
