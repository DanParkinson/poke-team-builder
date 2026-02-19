from src.extract.listings import extract_results_urls


def test_extract_results_urls_returns_all_urls():
    # Arrange
    page_json = {
        "results": [
            {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"},
            {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2/"},
        ]
    }

    # Act
    urls = extract_results_urls(page_json)

    # Assert
    assert urls == [
        "https://pokeapi.co/api/v2/pokemon/1/",
        "https://pokeapi.co/api/v2/pokemon/2/",
    ]


def test_extract_results_urls_returns_empty_list_when_no_results():
    # Arrange
    page_json = {}

    # Act
    urls = extract_results_urls(page_json)

    # Assert
    assert urls == []


def test_extract_results_urls_ignores_items_without_url():
    # Arrange
    page_json = {
        "results": [
            {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"},
            {"name": "invalid"},
        ]
    }

    # Act
    urls = extract_results_urls(page_json)

    # Assert
    assert urls == [
        "https://pokeapi.co/api/v2/pokemon/1/",
    ]
