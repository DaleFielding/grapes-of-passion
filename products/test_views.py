from django.test import TestCase
from django.urls import reverse
from .models import Product

class TestViews(TestCase):
    # Test product view
    def test_products_view(self):
        response = self.client.get(reverse('products'))  
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'products/products.html') 

    # Load fixtures for the below test
    fixtures = ['categories.json', 'products.json']  

    # Test product detail view
    def test_product_detail_view(self):
        product = Product.objects.get(pk=3)
        url = reverse('product_detail', args=[product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertContains(response, product.name)

