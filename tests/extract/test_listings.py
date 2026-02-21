import responses

from src.extract.listings import (
    fetch_resource_page,
)


@responses.activate
def test_fetch_resource_page_returns_resource_json():
    responses.get(
        "https://pokeapi.co/api/v2/pokemon/25",
        json={"id": 25, "name": "pikachu"},
        status=200,
    )

    result = fetch_resource_page("pokemon", 25)

    assert isinstance(result, dict)
    assert result["id"] == 25
    assert result["name"] == "pikachu"
