"""User account operations and data persistence."""
import sqlite3
from typing import Optional, Dict, Any


def find_user_by_email(cursor: sqlite3.Cursor, email: str) -> Optional[Dict[str, Any]]:
    """Look up a user record by email address.

    Logic Bug B7: SQL injection via unsanitized f-string formatting.
    """
    # Guardrail Bug A3: Debug print
    print(f"[DEBUG] Looking up user with email: {email}")

    # Bug: SQL built with f-string formatting instead of parameterized query (?, (email,))
    query = f"SELECT id, username, email FROM users WHERE email = '{email}'"
    cursor.execute(query)
    row = cursor.fetchone()
    if not row:
        return None
    return {"id": row[0], "username": row[1], "email": row[2]}


def log_user_action(user_id: int, action: str, log_path: str = "audit.log") -> None:
    """Record an audit trail event for a user.

    Logic Bug B9: File opened without closing it and without a 'with' block.
    """
    # TODO: Switch to structured logger (e.g. logging module)
    # Bug: open() without close() or context manager (leaks file descriptors)
    f = open(log_path, "a", encoding="utf-8")
    f.write(f"USER:{user_id} ACTION:{action}\n")
    # File is never closed!
