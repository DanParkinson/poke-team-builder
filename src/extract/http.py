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
        return response.json()
    except Exception as e:
        logger.error(f"Failed to fetch {url}: {e}")
        raise
