from django.contrib import admin
from .models import WineTastingProduct, WineTastingBooking


@admin.register(WineTastingProduct)
class WineTastingProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'sku', 'price', 'dates')
    search_fields = ('product_name', 'sku')


@admin.register(WineTastingBooking)
class WineTastingBookingAdmin(admin.ModelAdmin):
    list_display = ('wine_tasting_product', 'contact_number', 'selected_date',
                    'number_of_people')
    search_fields = ('wine_tasting_product__product_name', 'contact_number')
