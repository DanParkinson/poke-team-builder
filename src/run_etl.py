from src.utils.logger import get_logger


logger = get_logger(__name__)


def run_etl() -> None:
    """
    Main function for running ETL
    """

    logger.info("Beginning ETL Pipeline...")

    # raw_pokemon = extract_resource("pokemon")
    # transformed_pokemon = transform_pokemon_batch(raw_pokemon)

    logger.info("ETL run completed.")


if __name__ == "__main__":
    run_etl()
