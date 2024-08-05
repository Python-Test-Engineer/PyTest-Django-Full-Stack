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
list_tables = inspector.get_table_names()
apps_tables = filter(lambda x: x.startswith(("base_", "ecommerce_")), list_tables)
rprint(list(apps_tables))
print("=======================================================================")

print("\nRoom table")
table = "base_room"
# Get column information
columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
rprint(columns["id"])
assert columns["id"]["primary_key"] == 1  # i.e true


def test_0023_db_column_type():
    # Get column information
    # print("==========================")
    # print("\n\nis_trackid_integer")
    table = "base_room"
    columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
    assert isinstance(columns["id"]["type"], Integer), "Room Id should be an Integer"


# #  get FK
# def test_0024_db_artist_has_no_fk():
#     """Check Foreign Keys artist"""
#     # print("==========================")
#     # print("\n\nartists_has_no_fk")
#     table = "artists"
#     foreign_keys_artist = inspector.get_foreign_keys(table)
#     assert len(foreign_keys_artist) == 0
#     # rprint("Foreign Keys for artists?: ", foreign_keys_artist)


# def test_0025_db_track_has_fk():
#     # print("==========================")
#     # print("\n\ntrack_has_fk")
#     """Check Foreign Keys track - there is one track to artist"""
#     table = "tracks"
#     foreign_keys_track = inspector.get_foreign_keys(table)
#     assert len(foreign_keys_track) > 0


# def test_0026_db_nullables():
#     """Check trackid is not nullable"""
#     table = "tracks"
#     # Get column information
#     columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
#     assert columns["trackid"]["nullable"] is False


# def test_0027_db_primary_key():
#     """Check trackid is primary key"""
#     table = "tracks"
#     # Get column information
#     columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
#     assert columns["trackid"]["primary_key"] == 1  # i.e true


# def test_0028_db_default():
#     """Check trackid has default value"""
#     table = "tracks"
#     # Get column information
#     columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
#     assert columns["trackid"]["default"] is None
#     assert columns["trackname"]["default"] == "'TONY'"  # in db schema value is 'TONY'


# def test_0029_db_unique():
#     """
#     Check artistname is unique. N/A in SQLite
#     """
#     # table = "artists"
#     # # Get column information
#     # columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
#     # rprint(columns["artistname"])
#     # rprint("Check artistname is unique. N/A in SQLite.")
#     assert True
#     # assert columns["artistname"]["unique"] is True


# @pytest.mark.xfail
# def test_0030_db_check_constraint():
#     """
#     Check trackname has min 5 characters

#     """
#     table = "tracks"
#     # Get column information
#     columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
#     # print(
#     #     "In sqlite the CHECK constraint is not in the schema. It is, though, in the database."
#     # )
#     print("We could do an insert test to raise an exception.")
#     assert columns["trackname"]["check"] != ""
#     assert True
