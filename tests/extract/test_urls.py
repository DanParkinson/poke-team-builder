import pytest

from src.extract.urls import resource_url, BASE_URL


@pytest.mark.parametrize(
    "resource, resource_id, expected",
    [
        ("pokemon", None, f"{BASE_URL}/pokemon"),
        ("pokemon", 25, f"{BASE_URL}/pokemon/25"),
        ("ability", None, f"{BASE_URL}/ability"),
        ("ability", 1, f"{BASE_URL}/ability/1"),
        ("type", 999, f"{BASE_URL}/type/999"),
    ],
)
def test_resource_url_builds_correct_urls(resource, resource_id, expected):
    assert resource_url(resource, resource_id) == expected
