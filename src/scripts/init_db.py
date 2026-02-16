from src.utils.logger import get_logger
from src.database.connection import get_connection

logger = get_logger(__name__)


def main():
    logger.info("Initializing Database... ")
    try:
        with get_connection():
            pass
    except RuntimeError as e:
        logger.error(str(e))
        raise

    logger.info("Database initialized")


if __name__ == "__main__":
    main()
