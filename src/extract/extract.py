from src.extract.listings import fetch_resource_page, parse_page
from src.extract.http import fetch_json, fetch_json_batch
from utils.logger import get_logger

logger = get_logger(__name__)


def extract_resource(resource: str, resource_id: int | None = None) -> list[dict]:
    """
    Fetch JSON fromm the api

    Applied:
        - Single page extraction
        - Batch extraction

    Returns:
        A list of dictionaries of json data from specific resources.
        - Single: [{url1 data}]
        - Batch: [{url1 data, url2 data, url3 data, ...}]
    """
    if resource_id is not None:
        return extract_resource_single(resource, resource_id)
    else:
        urls = extract_resource_urls(resource)
        return fetch_json_batch(urls, resource)


def extract_resource_single(resource: str, resource_id: int) -> list[dict]:
    logger.info(f"Beginning single extraction of {resource} id={resource_id}...")
    return [fetch_resource_page(resource, resource_id)]


def extract_resource_urls(resource: str) -> list[dict]:
    """
    Fetches the initial resource page and goes through pages till end extracting all urls for resource.

    Initializes:
        - Total: count from the api to track progress

    Returns:
        - List of dict of urls
        e.g. [{'url1', 'url2', ...}]
    """
    logger.info(f"Beginning batch extraction of {resource} urls...")

    page = fetch_resource_page(resource)
    total = page.get("count", None)
    urls: list[str] = []

    while True:
        # Extract urls from results
        parsed = parse_page(page)
        urls.extend([item["url"] for item in parsed["results"]])

        log_progress(resource, collected=len(urls), total=total)

        next_url = parsed["next"]
        if next_url is None:
            break
        page = fetch_json(next_url)

    return urls


# ==============
# Helpers
# ==============


def log_progress(resource: str, collected: int, total: int | None = None) -> None:
    if total is not None:
        logger.info(f"collected {collected} / {total} {resource}")
    else:
        logger.info(f"collected {collected} {resource}")
