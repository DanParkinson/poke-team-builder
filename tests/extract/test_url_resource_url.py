from src.extract.urls import resource_url


def test_resource_url_builds_urls():
    # Arrange
    resource_1 = "pokemon"
    resource_2 = "type"
    resource_id_1 = 1
    resource_id_2 = 2
    # Act
    url_1 = resource_url(resource_1)
    url_2 = resource_url(resource_2)
    url_3 = resource_url(resource_1, resource_id_1)
    url_4 = resource_url(resource_2, resource_id_2)
    # Assert
    url_1 == "https://pokeapi.co/api/v2/pokemon"
    url_2 == "https://pokeapi.co/api/v2/type"
    url_3 == "https://pokeapi.co/api/v2/pokemon/1"
    url_4 == "https://pokeapi.co/api/v2/type/2"
