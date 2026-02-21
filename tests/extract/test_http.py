import pytest
import requests
import responses
from unittest.mock import Mock, patch


from src.extract.http import (
    fetch_json,
    fetch_json_batch,
)

# Fetch_json_batch
# test_fetch_json_batch_returns_list_of_json_records

# Fetch JSON
# - test_fetch_json_returns_dict_on_success
# - test_fetch_json_reraises_request_exception_on_http_error
# - test_fetch_json_raises_value_error_on_invalid_json


@responses.activate
def test_fetch_json_batch_returns_list_of_json_records():
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

    urls = [
        "https://pokeapi.co/api/v2/pokemon/1/",
        "https://pokeapi.co/api/v2/pokemon/2/",
    ]

    result = fetch_json_batch(urls, "pokemon")

    assert isinstance(result, list)
    assert len(result) == 2
    assert {item["id"] for item in result} == {1, 2}


def test_fetch_json_returns_dict_on_success():
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"ok": True}

    with patch("src.extract.http.requests.get", return_value=mock_response):
        result = fetch_json("https://example.com")

    assert result == {"ok": True}


def test_fetch_json_reraises_request_exception_on_http_error():
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.HTTPError("boom")

    with patch("src.extract.http.requests.get", return_value=mock_response):
        with pytest.raises(requests.RequestException):
            fetch_json("https://example.com")


def test_fetch_json_raises_value_error_on_invalid_json():
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.side_effect = ValueError("not json")

    with patch("src.extract.http.requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match=r"Invalid JSON returned from url="):
            fetch_json("https://example.com")
