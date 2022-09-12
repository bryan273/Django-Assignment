from django.test import TestCase
from django.urls import reverse, resolve
from katalog.views import show_katalog

class TestUrls(TestCase):
    def test_urls(self):
        url = reverse("katalog:show_katalog")
        self.assertEquals(resolve(url).func, show_katalog)