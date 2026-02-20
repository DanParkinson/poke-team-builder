from src.database.connection import get_connection
from src.utils.logger import get_logger
from src.contracts.contracts import REQUIRED_FIELDS_POKEMON

logger = get_logger(__name__)


def load_pokemon_batch(rows: dict) -> None:
    logger.info("Loading Pokemon into DataBase...")
    for row in rows:
        load_pokemon_row(row)
    logger.info("Pokemon table Loaded.")


def load_pokemon_row(row: dict) -> None:
    """
    Insert transformed pokemon data into DuckDB pokemon table
    """
    required = REQUIRED_FIELDS_POKEMON
    for field in required:
        if field not in row:
            raise ValueError(f"missing required field '{field}'")

    conn = get_connection()

    try:
        conn.execute("BEGIN")
        conn.execute(
            """
            INSERT INTO pokemon (id, name, base_experience, height, weight)
            VALUES(?, ?, ?, ?, ?)
            ON CONFLICT(id) DO NOTHING
            """,
            [
                row["id"],
                row["name"],
                row["base_experience"],
                row["height"],
                row["weight"],
            ],
        )
        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise
    finally:
        conn.close()
