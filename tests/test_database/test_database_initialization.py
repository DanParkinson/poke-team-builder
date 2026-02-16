import duckdb


def test_database_file_can_be_created(tmp_path):
    # Arrange
    db_path = tmp_path / "test.duckdb"

    # Act
    conn = duckdb.connect(str(db_path))
    conn.close()

    # Assert
    assert db_path.exists(), "DuckDb file was not created"


def test_database_connection_works(tmp_path):
    # Arrange
    db_path = tmp_path / "test.duckdb"
    conn = duckdb.connect(str(db_path))
    conn.close()

    # Act
    conn = duckdb.connect(str(db_path))
    result = conn.execute("SELECT 1").fetchone()
    conn.close()

    # Assert
    assert result == (1,)
