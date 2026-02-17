from src.utils.logger import get_logger
from src.database.connection import get_connection
from src.database.schema import SCHEMA_SQL

logger = get_logger(__name__)


def main():
    logger.info("Initializing Database... ")
    try:
        with get_connection() as conn:
            conn.execute(SCHEMA_SQL)
            tables = [t[0] for t in conn.execute("SHOW TABLES").fetchall()]

        logger.info(f"schema applied. TABLES: {tables}")
    except RuntimeError as e:
        logger.error(str(e))
        raise

    logger.info("Database initialized")


if __name__ == "__main__":
    main()
