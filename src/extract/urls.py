from urllib.parse import urlparse

BASE_URL = "https://pokeapi.co/api/v2"


def resource_url(resource: str) -> str:
    """Build a resource URL"""
    return f"{BASE_URL}/{resource}"


def parse_pokeapi_url(url: str) -> tuple[str, str]:
    """
    Return resource, ID from pokeAPI resource url.
    Example: https://pokeapi.co/api/v2/pokemon/1/ -> ('pokemon', 1)
    """
    path = urlparse(url).path.strip("/")  # 'api/v2/pokemon/1'
    parts = path.split("/")  # ['api', 'v2', 'pokemon', '1']

    resource = parts[-2]
    resource_id = int(parts[-1])
    return resource, resource_id
