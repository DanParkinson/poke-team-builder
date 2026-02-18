import requests

from utils.logger import get_logger

logger = get_logger(__name__)

BASE_URL = "https://pokeapi.co/api/v2"


def extract_pokemon(resource: str) -> None:
    """
    Fetch a pokemon data from the api as JSON.
    """
    page = fetch_resource_page(resource)
    urls = extract_results_urls(page)
    print(urls)


def extract_results_urls(page_json: dict) -> list[str]:
    results = page_json.get("results", [])
    return [item["url"] for item in results if "url" in item]


def fetch_resource_page(resource: str) -> dict:
    url = resource_url(resource)
    return fetch_json(url)


def resource_url(resource: str) -> str:
    """Build a resource URL"""
    return f"{BASE_URL}/{resource}"


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


if __name__ == "__main__":
    extract_pokemon("pokemon")
