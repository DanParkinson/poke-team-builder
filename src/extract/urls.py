BASE_URL = "https://pokeapi.co/api/v2"


def resource_url(resource: str, resource_id: int | None = None) -> str:
    """Build a resource URL"""
    if resource_id is not None:
        return f"{BASE_URL}/{resource}/{resource_id}"
    return f"{BASE_URL}/{resource}"
