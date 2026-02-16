"""Database models."""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from .database import Base
import os


class GameServer(Base):
    """GameServer model for managing game server instances."""

    __tablename__ = "game_servers"

    id = Column(Integer, primary_key=True, index=True)
    game_name = Column(String(255), nullable=False)
    instance_name = Column(String(255), nullable=True, unique=True)
    directory = Column(String(512), nullable=True)
    # config_path = Column(String(512), nullable=False)
    status = Column(String(50), nullable=False, default="offline")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def __init__(
        self, game_name, instance_name, directory, config_path, status="offline"
    ):
        self.game_name = game_name
        self.instance_name = instance_name
        self.directory = directory
        self.status = status

        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
            print(f"Created game directory at: {self.directory}")
        else:
            print(f"Game directory already exists at: {self.directory}")

    def __repr__(self):
        return f"<GameServer(id={self.id}, instance_name={self.instance_name}, game_name={self.game_name}, status={self.status})>"

    def to_dict(self):
        """Convert model to dictionary."""
        return {
            "id": self.id,
            "game_name": self.game_name,
            "instance_name": self.instance_name,
            "directory": self.directory,
            # "config_path": self.config_path,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
