from django.db import models
from django.contrib.auth.models import User


class WineTastingProduct(models.Model):
    product_name = models.CharField(max_length=100, null=False)
    sku = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dates = models.TextField()

    def __str__(self):
        return self.product_name


class WineTastingBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    wine_tasting_product = models.ForeignKey(WineTastingProduct,
                                             on_delete=models.CASCADE)
    special_requirements = models.TextField(null=True)
    number_of_people = models.IntegerField()
    contact_number = models.CharField(max_length=25, null=False)
    selected_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.wine_tasting_product.product_name} booking"
