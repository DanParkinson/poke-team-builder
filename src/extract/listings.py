from src.extract.http import fetch_json
from src.extract.urls import resource_url


def fetch_resource_page(resource: str) -> dict:
    url = resource_url(resource)
    return fetch_json(url)


def extract_results_urls(page_json: dict) -> list[str]:
    results = page_json.get("results", [])
    return [item["url"] for item in results if "url" in item]
