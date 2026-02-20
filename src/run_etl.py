from src.utils.logger import get_logger
from src.extract.extract import extract_resource
from src.transform.transform import transform_batch_pokemon
from src.load.pokemon import load_batch_pokemon


logger = get_logger(__name__)


def run_etl(resource: str, pokemon_id: int | None = None) -> None:
    """
    Main function for running ETL
    """
    logger.info("Beginning ETL Pipeline...")

    raw_pokemon = extract_resource(resource, pokemon_id)
    transformed_pokemon = transform_batch_pokemon(raw_pokemon)
    load_batch_pokemon(transformed_pokemon)

    logger.info("ETL run completed.")


if __name__ == "__main__":
    run_etl("pokemon", 1)
