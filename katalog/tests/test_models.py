from django.test import TestCase
from katalog.models import CatalogItem

class TestModels(TestCase):
    def setUp(self):
        CatalogItem.objects.create(item_name="Halo", item_price=5000000, item_stock=2, description="Yang beli berkah", rating=9, item_url="https://halo.com")

    def test_models(self):
        Halo = CatalogItem.objects.get(item_name="Halo")
        self.assertEquals(Halo.item_name, "Halo")
