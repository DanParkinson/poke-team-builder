def test_extract_resource_single(monkeypatch):
    expected = {"id": 1, "name": "bulbasaur"}

    monkeypatch.setattr(
        "src.extract.extract.fetch_resource_page",
        lambda resource, resource_id: expected,
    )

    from src.extract.extract import extract_resource

    result = extract_resource("pokemon", 1)

    assert result == [expected]


def test_extract_resource_batch(monkeypatch):
    urls = ["url1", "url2"]

    monkeypatch.setattr(
        "src.extract.extract.fetch_resource_page",
        lambda resource: {"results": [{"url": "url1"}, {"url": "url2"}]},
    )

    monkeypatch.setattr(
        "src.extract.extract.extract_results_urls",
        lambda page: urls,
    )

    monkeypatch.setattr(
        "src.extract.extract.fetch_json",
        lambda url: {"url": url},
    )

    from src.extract.extract import extract_resource

    result = extract_resource("pokemon")

    assert result == [{"url": "url1"}, {"url": "url2"}]
