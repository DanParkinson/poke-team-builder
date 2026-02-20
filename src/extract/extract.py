from src.extract.http import fetch_json
from src.extract.listings import fetch_resource_page, extract_results_urls
from utils.logger import get_logger

logger = get_logger(__name__)


def extract_resource(resource: str, resource_id: int | None = None) -> list[dict]:
    """
    Fetch batch data from the api as JSON.
    """
    if resource_id is not None:
        logger.info(f"Beginning single extraction of {resource} id={resource_id}...")
        return [fetch_resource_page(resource, resource_id)]

    logger.info(f"Beginning batch extraction of {resource} data...")
    page = fetch_resource_page(resource)
    urls = extract_results_urls(page)
    return [fetch_json(url) for url in urls]
