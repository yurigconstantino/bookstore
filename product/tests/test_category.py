from django.test import TestCase
import pytest
from product.models import Category

@pytest.mark.django_db
def test_category():
    category = Category.objects.create(
        title= 'produto_category',
        slug= '001'
    )

    assert category.title['title'] == 'produto_category'
    assert category.slug['slug'] == '001'
    assert category.description['description'] == 'essa é uma descrição'
    assert category.active['active'] == True