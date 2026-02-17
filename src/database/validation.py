def validate_schema(conn, EXPECTED_TABLES: set) -> None:
    """
    Raise RunTimeError if schema integrity check fails.
    """

    # Check basic query works
    conn.execute("SELECT 1").fetchone()

    # check tables exist
    tables = {t[0] for t in conn.execute("SHOW TABLES").fetchall()}
    missing = EXPECTED_TABLES - tables
    if missing:
        raise RuntimeError(f"Missing expected tables: {missing}")
