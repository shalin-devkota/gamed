"""Database module for gamed."""

from .database import (
    engine,
    Base,
    SessionLocal,
    get_db_session,
    close_db_session,
    initialize_database,
)
from .models import GameServer
from .db_gameserver import (
    register_gameserver,
    get_gameserver,
    get_gameserver_by_instance_name,
    get_all_gameservers,
    update_gameserver_status,
    delete_gameserver,
)

__all__ = [
    "engine",
    "Base",
    "SessionLocal",
    "get_db_session",
    "close_db_session",
    "GameServer",
    "register_gameserver",
    "get_gameserver",
    "get_gameserver_by_instance_name",
    "get_all_gameservers",
    "update_gameserver_status",
    "delete_gameserver",
]
