from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    # Test basket view
    def test_products_view(self):
        response = self.client.get(reverse('view_basket'))  
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'basket/basket.html') 