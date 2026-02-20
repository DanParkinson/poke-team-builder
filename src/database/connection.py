from pathlib import Path
import duckdb

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DB_PATH = PROJECT_ROOT / "data" / "pokemon.duckdb"


def get_connection() -> duckdb.DuckDBPyConnection:
    """
    Returns a connection to the project DuckDB database
    """
    try:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        return duckdb.connect(str(DB_PATH))
    except Exception as e:
        raise RuntimeError(f"Failed to connect to DuckDB at {DB_PATH.resolve()}") from e
