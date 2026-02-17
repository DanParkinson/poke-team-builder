from src.utils.logger import get_logger
from src.database.connection import get_connection
from src.database.migrate import apply_schema
from src.database.validation import validate_schema
from src.database.schema import SCHEMA_SQL, EXPECTED_TABLES

logger = get_logger(__name__)


def main():
    logger.info("Initializing Database... ")
    try:
        with get_connection() as conn:
            apply_schema(conn, SCHEMA_SQL)
            validate_schema(conn, EXPECTED_TABLES)
    except RuntimeError as e:
        logger.error(str(e))
        raise

    logger.info("Database initialized")


if __name__ == "__main__":
    main()
