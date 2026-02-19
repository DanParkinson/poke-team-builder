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


def test_fetch_json_raises_value_error_on_invalid_json(monkeypatch):
    class MockResponse:
        def raise_for_status(self):
            pass

        def json(self):
            raise ValueError("No JSON object could be decoded")

    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: MockResponse())

    with pytest.raises(ValueError, match="Invalid JSON returned"):
        fetch_json("https://pokeapi.co/api/v2/pokemon/1/")


def test_fetch_json_raises_on_request_exception(monkeypatch):
    def mock_get(*args, **kwargs):
        raise requests.Timeout("Timed out")

    monkeypatch.setattr(requests, "get", mock_get)

    with pytest.raises(requests.Timeout):
        fetch_json("https://pokeapi.co/api/v2/pokemon/1/")
