import pytest
from django.db import models

from base.models import User, Topic


def test_ORM_120_base_model_user_structure_table_exists():
    try:
        from base.models import User  # noqa F401

    except ImportError:
        assert False
    else:
        assert True


def test_ORM_121_base_model_topic_structure_table_exists():
    try:
        from base.models import Topic  # noqa F401

    except ImportError:
        assert False
    else:
        assert True


"""
- [ ] Validate the existence of expected columns in each table, ensuring correct data types.
"""


@pytest.mark.parametrize(
    "model, field_name, expected_type",
    [
        # (Users, "id", models.AutoField),
        (User, "name", models.CharField),
        (User, "email", models.EmailField),
        (User, "bio", models.TextField),
        (User, "avatar", models.ImageField),
    ],
)
def test_ORM_122_base_model_structure_column_data_types(
    model, field_name, expected_type
):
    assert hasattr(
        model, field_name
    ), f"{model.__name__} model does not have '{field_name} field"

    field = model._meta.get_field(field_name)

    assert isinstance(field, expected_type), f"Field is not type {expected_type}"


# """
# - [ ] Confirm expected field count
# """


@pytest.mark.parametrize(
    "model, expected_field_count",
    [
        (
            Topic,
            2,  # id field exists
        ),
    ],
)
def test_ORM_125_base_model_structure_field_count(model, expected_field_count):
    field_count = len(model._meta.fields)
    assert (
        field_count == expected_field_count
    ), f"{model.__name__} model has {field_count} fields, expected {expected_field_count}"


# # """
# # - [ ] Verify nullable or not nullable fields
# # """


@pytest.mark.parametrize(
    "model, field_name, expected_nullable",
    [
        (User, "id", False),
        (User, "name", True),
        (User, "email", True),
        (User, "bio", True),
        (User, "avatar", True),
    ],
)
def test_ORM_126_base_model_structure_nullable_constraints(
    model, field_name, expected_nullable
):
    # Get the field from the model
    field = model._meta.get_field(field_name)

    # Check if the nullable constraint matches the expected value
    assert (
        field.null is expected_nullable
    ), f"Field '{field_name}' has unexpected nullable constraint"


# # """
# # - [ ] Verify the correctness of default values for relevant columns.
# # """


@pytest.mark.parametrize(
    "model, field_name, expected_default_value",
    [
        (User, "avatar", "avatar.svg"),
    ],
)
def test_ORM_127_base_model_structure_default_values(
    model, field_name, expected_default_value
):
    # Get the field from the model
    field = model._meta.get_field(field_name)

    # Check if the default value matches the expected value
    default_value = field.default

    assert default_value == expected_default_value


# """
# - [ ] Ensure that column lengths align with defined requirements.
# """


@pytest.mark.parametrize(
    "model, field_name, expected_length",
    [
        (User, "name", 200),
        (Topic, "name", 200),
    ],
)
def test_ORM_128_base_model_structure_column_lengths(
    model, field_name, expected_length
):
    # Get the field from the model
    field = model._meta.get_field(field_name)

    # Check if the max length matches the expected value
    assert (
        field.max_length == expected_length
    ), f"Field '{field_name}' has unexpected max length"


# # """
# # - [ ] Validate the enforcement of unique constraints for columns requiring unique values.
# # """


@pytest.mark.parametrize(
    "model, field_name, is_unique",
    [
        (Topic, "id", True),
        (User, "id", True),
        # (Category, "slug", True),
        # (Category, "is_active", False),
        # (Category, "level", False),
    ],
)
def test_ORM_129_base_model_structure_unique_fields(model, field_name, is_unique):
    # Get the field from the model
    field = model._meta.get_field(field_name)

    # Check if the max length matches the expected value
    assert field.unique == is_unique, f"Field '{field_name}' uniqueness mismatch"
