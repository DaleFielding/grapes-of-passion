from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    def test_products_view(self):
        response = self.client.get(reverse('products'))  
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'products/products.html') 
