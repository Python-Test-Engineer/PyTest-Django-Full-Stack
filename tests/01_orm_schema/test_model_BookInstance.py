import pytest
from django.db import models

from catalog.models import BookInstance


def test_ORM_150_book_model_structure_table_exists():
    try:
        from catalog.models import BookInstance  # noqa F401
    except ImportError:
        assert False
    else:
        assert True


@pytest.mark.parametrize(
    "model, field_name, expected_nullable",
    [
        (BookInstance, "id", False),
        (BookInstance, "book", True),
        (BookInstance, "due_back", True),
        (BookInstance, "borrower", True),
    ],
)
def test_ORM_151_BookInstance_model_structure_nullable_constraints(
    model, field_name, expected_nullable
):
    # Get the field from the model
    field = model._meta.get_field(field_name)

    # Check if the nullable constraint matches the expected value
    assert (
        field.null is expected_nullable
    ), f"Field '{field_name}' has unexpected nullable constraint"


@pytest.mark.parametrize(
    "model, field_name, expected_type",
    [
        (BookInstance, "id", models.UUIDField),
        (BookInstance, "book", models.ForeignKey),
        (BookInstance, "due_back", models.DateField),
        (BookInstance, "imprint", models.CharField),
        (BookInstance, "borrower", models.ForeignKey),
    ],
)
def test_ORM_152_BookInstance_model_structure_column_data_types(
    model, field_name, expected_type
):
    assert hasattr(
        model, field_name
    ), f"{model.__name__} model does not have '{field_name} field"

    field = model._meta.get_field(field_name)

    assert isinstance(field, expected_type), f"Field is not type {expected_type}"


@pytest.mark.parametrize(
    "model, expected_field_count",
    [
        (
            BookInstance,
            6,
        ),
    ],
)
def test_ORM_153_BookInstance_model_structure_field_count(model, expected_field_count):
    field_count = len(model._meta.fields)
    assert (
        field_count == expected_field_count
    ), f"{model.__name__} model has {field_count} fields, expected {expected_field_count}"
