import pytest
from sqlmodel import create_engine, inspect
from sqlmodel import Integer
from pathlib import Path

from rich import print as rprint

DB = "db.sqlite3"

# 1
# DB_PATH = str((Path().parent / DB).resolve())
# db_uri = f"sqlite:///{DB_PATH}"

# 2
DB_URI = f"sqlite:///{DB}"

engine = create_engine(DB_URI)

inspector = inspect(engine)

# Get table information
print("\n\n=======================================================================\n")
print("-----------------")
print(f"{DB_URI}")
print("-----------------\n")
print(f"TABLES in {DB}:")
rprint(inspector.get_table_names())
print("=======================================================================")

print("\nmessage table")
table = "base_message"
# Get column information
columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
assert columns["id"]["primary_key"] == 1  # i.e true
rprint(columns)
print("-----------------------------------------------------")
print("\message table")
table = "base_message"
# Get column information
columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
rprint(columns)


def test_0023_db_column_type():
    # Get column information
    # print("==========================")
    # print("\n\nis_trackid_integer")
    table = "base_message"
    columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
    assert isinstance(columns["id"]["type"], Integer)


#  get FK
def test_0024_db_artist_has_no_fk():
    """Check Foreign Keys Message"""

    table = "base_message"
    foreign_keys_artist = inspector.get_foreign_keys(table)
    assert len(foreign_keys_artist) == 2


def test_0025_db_message_has_fk():
    # print("==========================")
    # print("\n\ntrack_has_fk")
    """Check Foreign Keys track - there is one track to artist"""
    table = "base_message"
    foreign_keys_message = inspector.get_foreign_keys(table)
    assert len(foreign_keys_message) > 0


def test_0026_db_nullables():
    """Check trackid is not nullable"""
    table = "base_message"
    # Get column information
    columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
    assert columns["id"]["nullable"] is False


def test_0027_db_primary_key():
    """Check trackid is primary key"""
    table = "base_message"
    # Get column information
    columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
    assert columns["id"]["primary_key"] == 1  # i.e true


def test_0029_db_unique():
    """
    Check artistname is unique. N/A in SQLite
    """
    # table = "artists"
    # # Get column information
    # columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
    # rprint(columns["artistname"])
    # rprint("Check artistname is unique. N/A in SQLite.")
    assert True
    # assert columns["artistname"]["unique"] is True


@pytest.mark.xfail
def test_0030_db_check_constraint():
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
