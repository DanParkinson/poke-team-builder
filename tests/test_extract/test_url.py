from src.extract.urls import parse_pokeapi_url, resource_url


def test_resource_url_builds_urls():
    # Arrange

    resource_1 = "pokemon"
    resource_2 = "type"
    # Act
    url_1 = resource_url(resource_1)
    url_2 = resource_url(resource_2)
    # Assert
    url_1 == "https://pokeapi.co/api/v2/pokemon"
    url_2 == "https://pokeapi.co/api/v2/type"


def test_parse_pokeapi_url_returns_resource_and_id():
    # Arrange
    url = "https://pokeapi.co/api/v2/pokemon/1/"

    # Act
    resource, resource_id = parse_pokeapi_url(url)

    # Assert
    assert resource == "pokemon"
    assert resource_id == 1
