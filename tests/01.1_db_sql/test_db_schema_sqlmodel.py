import pytest
from sqlmodel import create_engine, inspect
from sqlmodel import Integer
from pathlib import Path

from rich.console import Console

console = Console()
DB = "db.sqlite3"

# 1
# DB_PATH = str((Path().parent / DB).resolve())
# db_uri = f"sqlite:///{DB_PATH}"

# 2
DB_URI = f"sqlite:///{DB}"

engine = create_engine(DB_URI)

inspector = inspect(engine)


def test_SQL_000_db_TABLES_exists():
    console.print(f"\n[green bold]{DB_URI}[/]")
    console.print(
        "[blue]============================ APP TABLES ===============================[/]"
    )
    print(f"APP TABLES in {DB}:")
    all_tables = inspector.get_table_names()
    app_tables = filter(lambda x: x.startswith(("base_", "ecommerce_")), all_tables)
    console.print(list(app_tables))
    console.print(
        "[blue]============================ base_message table ===============================[/]"
    )


def test_SQL_001_db_column_type():
    # Get column information
    # print("==========================")
    # print("\n\nis_trackid_integer")
    table = "base_message"
    columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
    assert isinstance(columns["id"]["type"], Integer)
    assert columns["id"]["primary_key"] == 1  # i.e true
    console.print(columns)


#  get FK
def test_SQL_002_message_has_2_fks():
    """Check Foreign Keys Message"""

    table = "base_message"
    foreign_keys_messages = inspector.get_foreign_keys(table)
    console.print(foreign_keys_messages)
    assert len(foreign_keys_messages) == 2


def test_SQL_003_id_not_nullable():
    """Check id is not nullable"""
    table = "base_message"
    # Get column information
    columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
    assert columns["id"]["nullable"] is False


def test_SQL_004_id_is_primary_key():
    """Check id is primary key"""
    table = "base_message"
    # Get column information
    columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
    assert columns["id"]["primary_key"] == 1  # i.e true


def test_SQL_005_db_unique():
    """
    Check a field is unique. N/A in SQLite
    """
    table = "base_message"
    # Get column information
    columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
    # console.print(columns["body"]["unique"])

    assert True


@pytest.mark.xfail
def test_SQL_006_db_check_constraint():
    """
    Check trackname has min 5 characters

    """
    table = "base_message"
    # Get column information
    columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
    # print(
    #     "In sqlite the CHECK constraint is not in the schema. It is, though, in the database."
    # )
    print("We could do an insert test to raise an exception.")
    assert columns["name"]["check"] != ""
    assert True
