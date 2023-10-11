import pytest
from rest_framework.test import APITestCase, APIClient
from django.shortcuts import reverse
from conftest import EVERYTHING_EQUALS_NOT_NONE

pytestmark = [pytest.mark.django_db]


class GuestEndpointsTestCase(APITestCase):
    fixtures = ['catalog/tests/fixtures/categories_fixture.json',
                "catalog/tests/fixtures/discount_fixture.json",
                'catalog/tests/fixtures/product_fixture.json',
                'catalog/tests/fixtures/seller_fixture.json']


    def test_categories_list(self):
        url = reverse('categories')
        response = self.client.get(url)
        assert response.status_code == 200
        assert isinstance(response.data, list)
        assert response.data == [
            {
                "id": 1,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": EVERYTHING_EQUALS_NOT_NONE
            }
        ]


    def test_category_products(self):
        url = reverse('category-products', kwargs={'category_id': 1})
        response = self.client.get(url)

        assert response.status_code == 200
        assert response.data == [
            {
                "id": 1,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "price": "100.00",
                "articul": EVERYTHING_EQUALS_NOT_NONE,
                "description": EVERYTHING_EQUALS_NOT_NONE,
                "count_on_stock": EVERYTHING_EQUALS_NOT_NONE,
                "discount": EVERYTHING_EQUALS_NOT_NONE,
                "category": EVERYTHING_EQUALS_NOT_NONE,
                "seller": EVERYTHING_EQUALS_NOT_NONE
            }
        ]

        assert response.data[0]['discount'] == {
            "id": 1,
            "name": EVERYTHING_EQUALS_NOT_NONE,
            "date_start": EVERYTHING_EQUALS_NOT_NONE,
            "percent": 3,
            "date_end": EVERYTHING_EQUALS_NOT_NONE
        }