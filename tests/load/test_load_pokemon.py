import duckdb
import pytest

from src.database import connection as db_connection
from src.load.pokemon import load_pokemon_row
from src.database.schema import SCHEMA_SQL


@pytest.fixture
def test_db(tmp_path, monkeypatch):
    """
    Isolated temp DuckDB database with schema applied
    """
    db_path = tmp_path / "test_pokemon.duckdb"

    # patch app to use db_path
    monkeypatch.setattr(db_connection, "DB_PATH", db_path)

    # Schema
    conn = duckdb.connect(str(db_path))
    conn.execute(SCHEMA_SQL)
    conn.close()
    return db_path


def test_load_pokemon_row_inserts_one_row(test_db):
    row = {
        "id": 1,
        "name": "bulbasaur",
        "base_experience": 64,
        "height": 7,
        "weight": 69,
    }

    load_pokemon_row(row)

    conn = duckdb.connect(str(test_db))
    count = conn.execute("SELECT COUNT(*) FROM pokemon WHERE id = 1").fetchone()[0]
    conn.close()

    assert count == 1


def test_load_pokemon_row_is_idempotent(test_db):
    row = {
        "id": 1,
        "name": "bulbasaur",
        "base_experience": 64,
        "height": 7,
        "weight": 69,
    }

    load_pokemon_row(row)
    load_pokemon_row(row)

    conn = duckdb.connect(str(test_db))
    count = conn.execute("SELECT COUNT(*) FROM pokemon WHERE id = 1").fetchone()[0]
    total = conn.execute("SELECT COUNT(*) FROM pokemon").fetchone()[0]
    conn.close()

    assert count == 1
    assert total == 1


def test_load_pokemon_row_raises_on_missing_required_field(test_db):
    bad_row = {
        "id": 1,
        # "name" missing
        "base_experience": 64,
        "height": 7,
        "weight": 69,
    }

    with pytest.raises(ValueError, match="missing required field"):
        load_pokemon_row(bad_row)

    # Ensure nothing was inserted
    conn = duckdb.connect(str(test_db))
    total = conn.execute("SELECT COUNT(*) FROM pokemon").fetchone()[0]
    conn.close()

    assert total == 0


def test_load_pokemon_row_rolls_back_on_db_error(test_db):
    # name is NOT NULL in schema, so this should fail at the DB layer
    bad_row = {
        "id": 1,
        "name": None,
        "base_experience": 64,
        "height": 7,
        "weight": 69,
    }

    with pytest.raises(Exception):
        load_pokemon_row(bad_row)

    # Ensure nothing was inserted (rollback happened)
    conn = duckdb.connect(str(test_db))
    total = conn.execute("SELECT COUNT(*) FROM pokemon").fetchone()[0]
    conn.close()

    assert total == 0
