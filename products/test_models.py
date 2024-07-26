from django.test import TestCase
from .models import Category, Product


class CategoryModelTest(TestCase):
    # Create a category instance with the appropriate fields.
    def test_category_creation(self):
        category = Category.objects.create(
            name='Expected name',
            friendly_name='Expected friendly name'
        )
        # Checking if category was created with the expected fields
        self.assertEqual(category.name, 'Expected name')
        self.assertEqual(category.friendly_name, 'Expected friendly name')


class ProductModelTest(TestCase):

    # Specify the fixtures file to auto load the categories with Django
    fixtures = ['categories.json']

    def test_product_creation(self):
        # Get category from fixtures
        category = Category.objects.get(pk=1)
        # Create a product instance with the approproate fields
        product = Product.objects.create(
            category=category,
            sku='12345',
            name='Test Product',
            description='A product for testing purposes',
            price=9.99,
            discount=1.00,
            discounted_price=8.99,
            grape='Test Grape',
            country='Test Country',
            unit_volume=750.0,
            type='Test Type',
            alcohol_percentage=12.5,
            region_state='Test Region',
            style='Test Style',
            is_vegetarian=True,
            is_vegan=True,
            year=2020
        )
        # Asssertions to check if product was created with the expected fields
        self.assertEqual(product.category, category)
        self.assertEqual(product.sku, '12345')
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.description, 'A product for testing purposes')
        self.assertEqual(product.price, 9.99)
        self.assertEqual(product.discount, 1.00)
        self.assertEqual(product.discounted_price, 8.99)
        self.assertEqual(product.grape, 'Test Grape')
        self.assertEqual(product.country, 'Test Country')
        self.assertEqual(product.unit_volume, 750.0)
        self.assertEqual(product.type, 'Test Type')
        self.assertEqual(product.alcohol_percentage, 12.5)
        self.assertEqual(product.region_state, 'Test Region')
        self.assertEqual(product.style, 'Test Style')
        self.assertTrue(product.is_vegetarian)
        self.assertTrue(product.is_vegan)
        self.assertEqual(product.year, 2020)
        # Checking default image is set to none
        self.assertEqual(product.image, None)
