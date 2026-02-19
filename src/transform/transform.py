from src.utils.logger import get_logger

logger = get_logger(__name__)

REQUIRED_FIELDS = [
    "id",
    "name",
    "weight",
    "height",
    "base_experience",
]


def transform_pokemon_batch(raw_pokemon: list[dict]) -> list[dict]:
    logger.info(f"Transforming {len(raw_pokemon)} pokemon...")
    return [transform_pokemon(p) for p in raw_pokemon]


def transform_pokemon(data: dict) -> dict:
    pokemon_id = data.get("id", "unknown")
    pokemon_name = data.get("name", "unknown")

    logger.debug(f"Transforming pokemon id={pokemon_id}")

    for field in REQUIRED_FIELDS:
        if field not in data:
            raise ValueError(
                f"Pokemon transform failed for id={pokemon_id}, name='{pokemon_name}': "
                f"missing required field: '{field}'"
            )

    return {
        "id": data["id"],
        "name": data["name"],
        "weight": data["weight"],
        "height": data["height"],
        "base_experience": data["base_experience"],
    }
