import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "faker_pk.db")
_db_initialized = False


def ensure_db_exists():
    """Initialize the database if it does not exist yet."""
    global _db_initialized
    if _db_initialized:
        return
    if not os.path.exists(DB_PATH):
        try:
            from .initialize_db import initialize_database
            initialize_database(DB_PATH)
        except Exception as e:
            import warnings
            warnings.warn(f"faker-pk: could not auto-initialize database: {e}")
    _db_initialized = True


def _run(query, params, fetch):
    """Internal helper: open connection, run query, return fetched result."""
    ensure_db_exists()
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return fetch(cursor)


def query_value(query, params=()):
    """Return the first column of the first matching row."""
    row = _run(query, params, lambda c: c.fetchone())
    return row[0] if row else None


def query_row(query, params=()):
    """Return the first matching row as a tuple."""
    return _run(query, params, lambda c: c.fetchone())


def query_list(query, params=()):
    """Return a flat list of the first column from all matching rows."""
    return _run(query, params, lambda c: [r[0] for r in c.fetchall()])


def query_rows(query, params=()):
    """Return all matching rows as a list of tuples."""
    return _run(query, params, lambda c: c.fetchall())