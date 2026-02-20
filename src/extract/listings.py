from src.extract.http import fetch_json
from src.extract.urls import resource_url


def fetch_resource_page(resource: str, resource_id: int | None = None) -> dict:
    url = resource_url(resource, resource_id)
    return fetch_json(url)


def parse_page(page: dict) -> dict:
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


def extract_parsed_results_urls(results: list[dict]) -> list[str]:
    pass
