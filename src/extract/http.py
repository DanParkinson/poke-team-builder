import requests
from src.utils.logger import get_logger

logger = get_logger(__name__)


def fetch_json(url: str, timeout: float = 5.0) -> dict:
    """
    Fetches JSON DATA FROM API
    """
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"HTTP request failed for url = {url}: {e}")
        raise

    try:
        return response.json()
    except ValueError:
        logger.error(f"Invalid JSON response for url={url}")
        raise ValueError(f"Invalid JSON returned from url={url}")


def fetch_json_batch(urls: list[str], label: str, log_every: int = 20) -> list[dict]:
    """
    fetches json from list or urls

    Returns:
        - all JSON data from all of the urls

    Needs:
        - Optimizing
    """
    logger.info(f"Collected {len(urls)} detail URLs. Fetching detail JSON...")

    details: list[dict] = []
    total = len(urls)
    for i, url in enumerate(urls, start=1):
        details.append(fetch_json(url))

        if i % log_every == 0 or i == total:
            logger.info(f"Fetched detail {i}/{total} {label}")

    logger.info(f"Completed extraction of {len(details)} {label} details.")

    return details
