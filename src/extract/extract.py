from src.extract.http import fetch_json
from src.extract.urls import parse_pokeapi_url
from src.extract.listings import fetch_resource_page, extract_results_urls
from utils.logger import get_logger

logger = get_logger(__name__)

BASE_URL = "https://pokeapi.co/api/v2"


def extract_pokemon(resource: str) -> None:
    """
    Fetch a pokemon data from the api as JSON.
    """
    logger.info("Beginning extraction of Pokemon data...")
    page = fetch_resource_page(resource)
    urls = extract_results_urls(page)
    for url in urls:
        resource, resource_id = parse_pokeapi_url(url)
        data = fetch_json(url)
        print(
            resource_id,
            data["name"],
            data["height"],
            data["weight"],
            data["base_experience"],
        )

    logger.info("pokemon data successfully extracted.")


if __name__ == "__main__":
    extract_pokemon("pokemon")
