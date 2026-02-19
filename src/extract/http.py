import requests

from utils.logger import get_logger

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
