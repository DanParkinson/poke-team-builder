from src.extract.http import fetch_json
from src.extract.listings import fetch_resource_page, extract_results_urls
from utils.logger import get_logger

logger = get_logger(__name__)

BASE_URL = "https://pokeapi.co/api/v2"


def extract_resource(resource: str) -> None:
    """
    Fetch a pokemon data from the api as JSON.
    """
    logger.info(f"Beginning extraction of {resource} data...")
    page = fetch_resource_page(resource)
    urls = extract_results_urls(page)

    resources: list[dict] = []

    for url in urls:
        data = fetch_json(url)
        resources.append(data)

    logger.info(f"{resource} data successfully extracted.")
    return resources
