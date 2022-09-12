from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    def test_views(self):
        client = Client()
        response = client.get(reverse("katalog:show_katalog"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "katalog.html")