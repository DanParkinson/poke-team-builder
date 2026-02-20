from src.extract.http import fetch_json
from src.extract.listings import fetch_resource_page, parse_page
from utils.logger import get_logger

logger = get_logger(__name__)


def extract_resource(resource: str, resource_id: int | None = None) -> list[dict]:
    """
    Fetch data from the api as JSON.
    """
    if resource_id is not None:
        logger.info(f"Beginning single extraction of {resource} id={resource_id}...")
        return [fetch_resource_page(resource, resource_id)]

    logger.info(f"Beginning batch extraction of {resource} data...")

    page = fetch_resource_page(resource)
    parsed = parse_page(page)
    total = page.get("count", None)
    urls: list[str] = []

    while True:
        # Extract urls from results
        parsed = parse_page(page)
        urls.extend([item["url"] for item in parsed["results"]])

        if total is not None:
            logger.info(f"collected {len(urls)} / {total} {resource}")
        else:
            logger.info(f"collected {len(urls)} {resource}")
        next_url = parsed["next"]

        if next_url is None:
            break
        page = fetch_json(next_url)

    logger.info(f"Collected {len(urls)} detail URLs. Fetching detail JSON...")
    details: list[dict] = []
    total_details = len(urls)

    for i, url in enumerate(urls, start=1):
        # fetch json from each url
        details.append(fetch_json(url))

        if i % 20 == 0 or i == total_details:
            logger.info(f"Fetched detail {i}/{total_details} {resource}")

    logger.info(f"Completed extraction of {total_details} {resource} details.")
    return details
