from django.test import TestCase

# Create your tests here.
import pytest

from order.models import User


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create(
    email = "user-email",
    username = "username",
)

    assert user.username == "username"
    assert user.email == "user-email"
