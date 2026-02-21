import responses

from src.extract.extract import extract_resource, extract_resource_urls

# Core functionality
# - test_extract_resource_single_returns_one_record
# - test_extract_resource_batch_returns_many_records
# - test_extract_resource_urls_follows_next_links_until_exhausted():


@responses.activate
def test_extract_resource_single_returns_one_record():
    responses.get(
        "https://pokeapi.co/api/v2/pokemon/25",
        json={"id": 25, "name": "pikachu"},
        status=200,
    )

    result = extract_resource("pokemon", resource_id=25)

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["id"] == 25
    assert result[0]["name"] == "pikachu"


@responses.activate
def test_extract_resource_batch_returns_many_records():
    # Listing page (first page, no pagination)
    responses.get(
        "https://pokeapi.co/api/v2/pokemon",
        json={
            "count": 2,
            "next": None,
            "results": [
                {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"},
                {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2/"},
            ],
        },
        status=200,
    )

    # Detail pages
    responses.get(
        "https://pokeapi.co/api/v2/pokemon/1/",
        json={"id": 1, "name": "bulbasaur"},
        status=200,
    )
    responses.get(
        "https://pokeapi.co/api/v2/pokemon/2/",
        json={"id": 2, "name": "ivysaur"},
        status=200,
    )

    result = extract_resource("pokemon")

    assert isinstance(result, list)
    assert len(result) == 2
    assert {item["id"] for item in result} == {1, 2}


@responses.activate
def test_extract_resource_urls_follows_next_links_until_exhausted():
    # Page 1
    responses.get(
        "https://pokeapi.co/api/v2/pokemon",
        json={
            "count": 3,
            "next": "https://pokeapi.co/api/v2/pokemon?offset=2",
            "results": [
                {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"},
                {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2/"},
            ],
        },
        status=200,
    )

    # Page 2 (last page)
    responses.get(
        "https://pokeapi.co/api/v2/pokemon?offset=2",
        json={
            "count": 3,
            "next": None,
            "results": [
                {"name": "venusaur", "url": "https://pokeapi.co/api/v2/pokemon/3/"},
            ],
        },
        status=200,
    )

    urls = extract_resource_urls("pokemon")

    assert urls == [
        "https://pokeapi.co/api/v2/pokemon/1/",
        "https://pokeapi.co/api/v2/pokemon/2/",
        "https://pokeapi.co/api/v2/pokemon/3/",
    ]
