from src.extract.urls import resource_url


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
