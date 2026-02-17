def apply_schema(conn, SCHEMA: str) -> None:
    conn.execute(SCHEMA)


def rebuild_schema(conn, DROP: str, SCHEMA: str) -> None:
    conn.execute(DROP)
    conn.execute(SCHEMA)
