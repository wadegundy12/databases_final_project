# db.py
import sqlite3
import bcrypt  

DB_NAME = "users.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    """
    Create the users table if it does not exist.
    Columns:
      - username (PRIMARY KEY)
      - password (bcrypt hash, stored as BLOB)
      - wins (int, default 0)
      - losses (int, default 0)
    """
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password BLOB NOT NULL,
            wins     INTEGER NOT NULL DEFAULT 0,
            losses   INTEGER NOT NULL DEFAULT 0
        )
        """
    )

    conn.commit()
    conn.close()


def user_exists(username: str) -> bool:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    row = cur.fetchone()

    conn.close()
    return row is not None


def create_new_user(username: str, password: str) -> None:
    """
    Create a new user with a bcrypt-hashed password and 0 wins/losses.
    """
    conn = get_connection()
    cur = conn.cursor()

    pw_bytes = password.encode("utf-8")
    hashed = bcrypt.hashpw(pw_bytes, bcrypt.gensalt())

    cur.execute(
        "INSERT INTO users (username, password, wins, losses) VALUES (?, ?, 0, 0)",
        (username, hashed),
    )

    conn.commit()
    conn.close()


def validate_login(username: str, password: str) -> bool:
    """
    Return True if username exists and bcrypt says the password matches.
    """
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT password FROM users WHERE username = ?",
        (username,),
    )
    row = cur.fetchone()
    conn.close()

    if row is None:
        return False

    stored_hash = row[0]          
    pw_bytes = password.encode("utf-8")


    return bcrypt.checkpw(pw_bytes, stored_hash)


def record_result(winner_username: str, loser_username: str) -> None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE users SET wins = wins + 1 WHERE username = ?",
        (winner_username,),
    )
    cur.execute(
        "UPDATE users SET losses = losses + 1 WHERE username = ?",
        (loser_username,),
    )

    conn.commit()
    conn.close()


def get_stats(username: str):
    """
    Return (wins, losses) for a user, or (0, 0) if not found.
    """
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT wins, losses FROM users WHERE username = ?",
        (username,),
    )
    row = cur.fetchone()
    conn.close()

    if row is None:
        return 0, 0
    return row[0], row[1]
