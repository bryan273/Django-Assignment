from django.test import TestCase
from katalog.models import CatalogItem

class TestModels(TestCase):
    def setUp(self):
        CatalogItem.objects.create(item_name="Teman", item_price=10000000, item_stock=1, description="Saya belikan ice cream kamu", rating=9, item_url="https://hokben.com")

    def test_models(self):
        temen = CatalogItem.objects.get(item_name="Teman")
        self.assertEquals(temen.item_name, "Teman")