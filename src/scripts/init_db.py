from pathlib import Path
import duckdb

from src.utils.logger import get_logger

logger = get_logger(__name__)
DB_PATH = Path("data/pokemon.duckdb")


def main():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = duckdb.connect(str(DB_PATH))
    conn.close()

    logger.info(f"Database created at {DB_PATH.resolve()}")


if __name__ == "__main__":
    main()
