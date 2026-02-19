from src.extract.http import fetch_json
from src.extract.urls import resource_url


def fetch_resource_page(resource: str) -> dict:
    url = resource_url(resource)
    return fetch_json(url)


def extract_results_urls(page_json: dict) -> list[str]:
    if "results" not in page_json:
        raise ValueError("Listing extraction failed: missing 'results' field")

    results = page_json["results"]

    if not isinstance(results, list):
        raise ValueError("Listing extraction failed: 'results' must be a list")

    urls = []

    for i, item in enumerate(results):
        if "url" not in item:
            raise ValueError(
                f"Listing extraction failed: missing 'url' in results[{i}]"
            )

        urls.append(item["url"])

    return urls
