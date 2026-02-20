from src.database.connection import get_connection
from src.utils.logger import get_logger
from src.contracts.contracts import REQUIRED_FIELDS_POKEMON

logger = get_logger(__name__)


def load_batch_pokemon(rows: dict) -> None:
    logger.info("Loading Pokemon into DataBase...")
    inserted_count = 0
    skipped_count = 0
    for row in rows:
        if load_pokemon_row(row):
            inserted_count += 1
        else:
            skipped_count += 1
    logger.info(
        f"Pokemon table loaded. inserted={inserted_count}, skipped={skipped_count}"
    )


def load_pokemon_row(row: dict) -> bool:
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
        result = conn.execute(
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
        inserted = result.rowcount == 1

        if inserted:
            logger.debug(f"Inserted pokemon id={row['id']}")
        else:
            logger.debug(f"Skipped pokemon id={row['id']} (already exists)")

    except Exception:
        conn.execute("ROLLBACK")
        raise
    finally:
        conn.close()
