import pytest
from pytest_django.asserts import assertTemplateUsed, assertTemplateNotUsed


@pytest.fixture
def maintenance_mode_on(settings):
    # settings is a built in fixture when using pytest-django
    settings.MAINTENANCE_MODE = True


@pytest.fixture
def maintenance_mode_off(settings):
    # settings is a built in fixture when using pytest-django
    settings.MAINTENANCE_MODE = False


# We cannot use RequestFactory as RF does not use middleware


def test_MSC_503_response_when_maintenance_mode_is_on(maintenance_mode_on, client):
    respone = client.get("/")
    response_text = "Application is in maintenance mode."
    assert response_text in respone.content.decode("utf-8")
    assertTemplateUsed(respone, "maintenance_mode_on.html")


def test_MSC_504_response_when_maintenance_mode_is_off(maintenance_mode_off, client):
    respone = client.get("/")
    response_text = "Application is in maintenance mode."
    assert response_text not in respone.content.decode("utf-8")
    assertTemplateNotUsed(respone, "maintenance_mode_on.html")
