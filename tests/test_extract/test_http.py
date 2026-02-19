import requests
import pytest
from src.extract.http import fetch_json


def test_fetch_json_returns_dict_on_success(monkeypatch):
    # Arrange
    expected = {"name": "bulbasaur"}

    class MockResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return expected

    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: MockResponse())

    # Act
    result = fetch_json("https://pokeapi.co/api/v2/pokemon/1/")

    # Assert
    assert result == expected


def test_fetch_json_raises_on_http_error(monkeypatch):
    class MockResponse:
        def raise_for_status(self):
            raise requests.HTTPError("404 error")

        def json(self):
            return {}

    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: MockResponse())

    with pytest.raises(requests.HTTPError):
        fetch_json("https://pokeapi.co/api/v2/pokemon/9999/")
