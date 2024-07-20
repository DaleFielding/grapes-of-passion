from django.db import models

class WineTastingProduct(models.Model):
    product_name = models.CharField(max_length=100, null=False)
    sku = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dates = models.TextField()

    def __str__(self):
        return self.product_name
