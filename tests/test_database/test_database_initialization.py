from src.database.connection import get_connection


def test_get_connection_returns_valid_connection():
    # Act
    conn = get_connection()
    result = conn.execute("SELECT 1").fetchone()
    conn.close()

    # Assert
    assert result == (1,)
