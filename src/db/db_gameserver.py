from typing import Optional, List
from sqlalchemy.exc import SQLAlchemyError
from .database import get_db_session, close_db_session
from .models import GameServer


def register_gameserver(
    game_name: str,
    instance_name: str,
    directory: str,
    config_path: str,
    status: str = "offline",
) -> Optional[GameServer]:
    """
    Register a new game server.

    Args:
        game_name: Name of the game
        instance_name: Unique name for the server instance
        directory: Directory path of the server
        config_path: Path to the configuration file
        status: Server status (default: "offline")

    Returns:
        GameServer object if successful, None if failed
    """
    session = get_db_session()
    try:
        game_server = GameServer(
            game_name=game_name,
            instance_name=instance_name,
            directory=directory,
            config_path=config_path,
            status=status,
        )
        session.add(game_server)
        session.commit()
        session.refresh(game_server)
        return game_server
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error registering game server: {e}")
        return None
    finally:
        close_db_session(session)


def get_gameserver(gameserver_id: int) -> Optional[GameServer]:
    """
    Get a game server by ID.

    Args:
        gameserver_id: ID of the game server

    Returns:
        GameServer object or None if not found
    """
    session = get_db_session()
    try:
        return session.query(GameServer).filter(GameServer.id == gameserver_id).first()
    finally:
        close_db_session(session)


def get_gameserver_by_instance_name(instance_name: str) -> Optional[GameServer]:
    """
    Get a game server by instance name.

    Args:
        instance_name: Name of the server instance

    Returns:
        GameServer object or None if not found
    """
    session = get_db_session()
    try:
        return (
            session.query(GameServer)
            .filter(GameServer.instance_name == instance_name)
            .first()
        )
    finally:
        close_db_session(session)


def get_or_create_gameserver(
    game_name: str,
    instance_name: str,
    directory: str,
    config_path: str,
) -> Optional[GameServer]:
    """
    Get a game server by instance name, or create it if it doesn't exist.

    This is useful when starting a server - it ensures the server entry exists in the DB
    and returns the entry for use in the startup process.

    Args:
        game_name: Name of the game
        instance_name: Unique name for the server instance
        directory: Directory path of the server
        config_path: Path to the configuration file

    Returns:
        GameServer object if found or created successfully, None if failed
    """
    session = get_db_session()
    try:
        # Check if server already exists
        game_server = (
            session.query(GameServer)
            .filter(GameServer.instance_name == instance_name)
            .first()
        )

        if game_server:
            # Server exists, return it
            return game_server
        else:
            # Server doesn't exist, create it
            game_server = GameServer(
                game_name=game_name,
                instance_name=instance_name,
                directory=directory,
                config_path=config_path,
                status="offline",
            )
            session.add(game_server)
            session.commit()
            session.refresh(game_server)
            print(f"Created new game server entry: {instance_name}")
            return game_server
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error getting or creating game server: {e}")
        return None
    finally:
        close_db_session(session)


def get_all_gameservers() -> List[GameServer]:
    """
    Get all game servers.

    Returns:
        List of GameServer objects
    """
    session = get_db_session()
    try:
        return session.query(GameServer).all()
    finally:
        close_db_session(session)


def update_gameserver_status(gameserver_id: int, status: str) -> Optional[GameServer]:
    """
    Update the status of a game server.

    Args:
        gameserver_id: ID of the game server
        status: New status

    Returns:
        Updated GameServer object or None if not found
    """
    session = get_db_session()
    try:
        game_server = (
            session.query(GameServer).filter(GameServer.id == gameserver_id).first()
        )
        if game_server:
            game_server.status = status
            session.commit()
            session.refresh(game_server)
            return game_server
        return None
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error updating game server status: {e}")
        return None
    finally:
        close_db_session(session)


def delete_gameserver(gameserver_id: int) -> bool:
    """
    Delete a game server.

    Args:
        gameserver_id: ID of the game server

    Returns:
        True if successful, False otherwise
    """
    session = get_db_session()
    try:
        game_server = (
            session.query(GameServer).filter(GameServer.id == gameserver_id).first()
        )
        if game_server:
            session.delete(game_server)
            session.commit()
            return True
        return False
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error deleting game server: {e}")
        return False
    finally:
        close_db_session(session)
