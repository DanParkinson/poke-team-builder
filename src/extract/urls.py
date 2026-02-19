BASE_URL = "https://pokeapi.co/api/v2"


def resource_url(resource: str) -> str:
    """Build a resource URL"""
    return f"{BASE_URL}/{resource}"
