from pathlib import Path
import os
import pytest
import sqlite3
from django.conf import settings
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

DB_SETTINGS = settings.DATABASES["default"]["NAME"]
DB_PATH = str(os.path.abspath(DB_SETTINGS))
console.print(f"[cyan bold]DB_PATH: {DB_PATH}[/]")


def test_SQL_0011_db_TABLES_exists():
    console.print(f"\n[green bold]{DB_URI}[/]")
    console.print(
        "[blue]============================ APP TABLES ===============================[/]"
    )
    print(f"Catalog tables in {DB}:")
    all_tables = inspector.get_table_names()
    app_tables = filter(lambda x: x.startswith(("catalog_",)), all_tables)
    console.print(list(app_tables))
    console.print(
        "[blue]============================ base_message table ===============================[/]"
    )


#  get FKs
def test_SQL_012_BookInstance_has_2_fks():
    """Check Foreign Keys Message"""

    table = "catalog_bookinstance"
    foreign_keys_messages = inspector.get_foreign_keys(table)
    console.print(foreign_keys_messages)
    assert len(foreign_keys_messages) == 2


def test_SQL_013_id_not_nullable():
    """Check id is not nullable"""
    table = "catalog_bookinstance"
    # Get column information
    columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
    assert columns["due_back"]["nullable"] is True
    assert columns["id"]["nullable"] is False


def test_SQL_014_execute_sql():
    """We can run SQL queries natively. SQLite does not support stored procedures

    If we have appropriate SQL Schema queries, we can use them to test DB Schema.
    """
    try:
        sqliteConnection = sqlite3.connect(DB_PATH)
        cursor = sqliteConnection.cursor()
        console.print(
            f"\n[green bold]{DB} created and Successfully Connected to SQLite[/]"
        )

        sql = "SELECT * FROM catalog_author"
        cursor.execute(sql)
        records = cursor.fetchall()
        print("\n")
        console.print(list(records))

        cursor.close()

    except sqlite3.Error as error:
        console.print("\n[red]Error while connecting to sqlite[/red]", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            console.print("[green bold]The SQLite connection is closed[/]")


# def test_SQL_004_field_unique():
#     """
#     Check a field is unique. N/A in SQLite
#     """
#     table = "catalog_book"
#     # Get column information
#     columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
#     print("\nProperties in catalog_book:")
#     for column in columns:
#         for prop in columns[column]:
#             if column == "isbn":
#                 print(f"{prop}")
# assert columns["isbn"]["unique"] is True # test not available in sqlite schema?


# @pytest.mark.xfail
# def test_SQL_006_db_check_constraint():
#     """
#     Check trackname has min 5 characters

#     """
#     table = "base_message"
#     # Get column information
#     columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
#     # print(
#     #     "In sqlite the CHECK constraint is not in the schema. It is, though, in the database."
#     # )
#     print("We could do an insert test to raise an exception.")
#     assert columns["name"]["check"] != ""
#     assert True
