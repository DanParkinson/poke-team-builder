import duckdb

from src.database.connection import get_connection
from src.database.migrate import apply_schema, rebuild_schema
from src.database.schema import SCHEMA_SQL


def test_get_connection_returns_valid_connection():
    # Act
    conn = get_connection()
    result = conn.execute("SELECT 1").fetchone()
    conn.close()

    # Assert
    assert result == (1,)


def test_schema_creates_tables(tmp_path):
    # Arrange
    db_path = tmp_path / "test.duckdb"
    expected = {"pokemon", "pokemon_stats", "pokemon_types", "type_chart"}
    conn = duckdb.connect(str(db_path))

    # Act
    apply_schema(conn, SCHEMA_SQL)
    tables = {t[0] for t in conn.execute("SHOW TABLES").fetchall()}
    conn.close()

    # Assert
    assert expected.issubset(tables)


def test_apply_schema_twice_does_not_error(tmp_path):
    # Arrange
    db_path = tmp_path / "test.duckdb"
    conn = duckdb.connect(str(db_path))

    # Act
    apply_schema(conn, SCHEMA_SQL)
    apply_schema(conn, SCHEMA_SQL)
    conn.close()

    # Assert
    assert True


def test_rebuild_schema_drops_existing_tables(tmp_path):
    # Arrange
    db_path = tmp_path / "test.duckdb"
    conn = duckdb.connect(str(db_path))

    SCHEMA_TEST = """
    CREATE TABLE pokemon (id INTEGER PRIMARY KEY, name TEXT)
    """

    DROP_TEST = """
    DROP TABLE IF EXISTS pokemon;
    """

    apply_schema(conn, SCHEMA_TEST)
    conn.execute("INSERT INTO pokemon VALUES (1, 'bulbasaur')")

    # Act
    rebuild_schema(conn, DROP_TEST, SCHEMA_TEST)
    count = conn.execute("SELECT COUNT(*) FROM pokemon").fetchone()[0]
    conn.close()

    # Assert
    assert count == 0
