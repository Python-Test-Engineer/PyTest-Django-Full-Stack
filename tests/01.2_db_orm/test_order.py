import pytest
from django.db import models

from ecommerce.models import Category, Product, Order


def test_ORM_150_order_model_structure_table_exists():
    try:
        from ecommerce.models import Order  # noqa F401
    except ImportError:
        assert False
    else:
        assert True


@pytest.mark.parametrize(
    "model, field_name, expected_nullable",
    [
        (Order, "order_id", False),
        (Order, "user", False),
        (Order, "product", False),
        (Order, "quantity", False),
    ],
)
def test_ORM_151_order_model_structure_nullable_constraints(
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
        (Order, "order_id", models.AutoField),
        (Order, "user", models.ForeignKey),
        (Order, "product", models.ForeignKey),
        (Order, "quantity", models.IntegerField),
    ],
)
def test_ORM_152_order_model_structure_column_data_types(
    model, field_name, expected_type
):
    assert hasattr(
        model, field_name
    ), f"{model.__name__} model does not have '{field_name} field"

    field = model._meta.get_field(field_name)

    assert isinstance(field, expected_type), f"Field is not type {expected_type}"


"""
- [ ] Confirm expected field count
"""
