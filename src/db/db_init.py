import sqlite3


def initialize_database():
    conn = sqlite3.connect("gamed.db")
    c = conn.cursor()

    # Create servers table
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS servers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            game_name TEXT NOT NULL,
            instance_name TEXT NOT NULL,
            directory TEXT NOT NULL,
            config_path TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """
    )

    conn.commit()
    conn.close()
