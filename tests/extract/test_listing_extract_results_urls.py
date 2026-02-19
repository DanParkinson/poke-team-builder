import pytest

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

    with pytest.raises(ValueError, match="missing 'results'"):
        extract_results_urls(page_json)


def test_extract_results_urls_raises_when_url_missing():
    page_json = {
        "results": [
            {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"},
            {"name": "invalid"},
        ]
    }

    with pytest.raises(ValueError, match="missing 'url'"):
        extract_results_urls(page_json)
