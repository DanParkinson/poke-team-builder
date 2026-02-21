from src.extract.urls import resource_url
from src.extract.http import fetch_json
from src.utils.logger import get_logger


logger = get_logger(__name__)


def fetch_resource_page(resource: str, resource_id: int | None = None) -> dict:
    url = resource_url(resource, resource_id)
    return fetch_json(url)


def parse_page(page: dict) -> dict:
    """
    Parse a resource listing page safely.


    """
    results = [
        {
            "name": item["name"],
            "url": item["url"],
        }
        for item in page["results"]
    ]

    next_url = page.get("next")

    return {
        "results": results,
        "next": next_url,
    }
