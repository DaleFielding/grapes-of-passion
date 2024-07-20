from django.contrib import admin
from .models import WineTastingProduct

@admin.register(WineTastingProduct)
class WineTastingProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'sku', 'price', 'dates')
    search_fields = ('product_name', 'sku')
