import pytest

from src.transform.transform import transform_pokemon


def make_valid(**overrides):
    payload = {
        "id": 1,
        "name": "bulbasaur",
        "weight": 69,
        "height": 7,
        "base_experience": 64,
    }
    payload.update(overrides)
    return payload


def test_transform_pokemon_success():
    result = transform_pokemon(make_valid())
    assert result == {
        "id": 1,
        "name": "bulbasaur",
        "weight": 69,
        "height": 7,
        "base_experience": 64,
    }


def test_transform_pokemon_error_includes_id_and_name_when_present():
    payload = make_valid()
    payload.pop("weight")

    with pytest.raises(ValueError) as excinfo:
        transform_pokemon(payload)

    msg = str(excinfo.value)
    assert "id=1" in msg
    assert "name='bulbasaur'" in msg


@pytest.mark.parametrize(
    "missing_field", ["id", "name", "weight", "height", "base_experience"]
)
def test_transform_pokemon_missing_required_field_raises_value_error(missing_field):
    payload = make_valid()
    payload.pop(missing_field)

    with pytest.raises(ValueError) as excinfo:
        transform_pokemon(payload)

    msg = str(excinfo.value)
    assert "Pokemon transform failed" in msg
    assert f"missing required field: '{missing_field}'" in msg


def test_transform_pokemon_error_uses_unknown_when_id_and_name_missing():
    payload = make_valid()
    payload.pop("id")
    payload.pop("name")

    with pytest.raises(ValueError) as excinfo:
        transform_pokemon(payload)

    msg = str(excinfo.value)
    assert "id=unknown" in msg
    assert "name='unknown'" in msg
