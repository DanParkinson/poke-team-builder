import duckdb

from src.database.connection import get_connection
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
    conn.execute(SCHEMA_SQL)
    tables = {t[0] for t in conn.execute("SHOW TABLES").fetchall()}
    conn.close()

    # Assert
    assert expected.issubset(tables)
