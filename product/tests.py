from django.test import TestCase

# Create your tests here.
import pytest

from product.models import Product


@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(
        title="Product name",
        description="Product descriction",
        price=999
    )

    assert product.title == "Product name"
    assert product.description == "Product descriction"
    assert product.price == 999