from django.test import TestCase
from .models import Category, Product


class CategoryModelTest(TestCase):
    # Testing if a category can be created and with the appropriate fields.
    def test_category_creation(self):
        category = Category.objects.create(
            name='Expected name',
            friendly_name='Expected friendly name'
        )
        # Checking if category was created with the expected fields
        self.assertEqual(category.name, 'Expected name')
        self.assertEqual(category.friendly_name,  5)