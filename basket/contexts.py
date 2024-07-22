from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def basket_contents(request):
    """
    Return basket contents and totals for use in all templates
    """
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    wine_items = []
    wine_categories = ['red', 'white', 'rose']

    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            if product.category.name.lower() in wine_categories:
                wine_items.extend([product] * item_data)
            total += item_data * product.price
            product_count += item_data
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)

    # 5 for 4 wine bottles discount calculation
    discount = 0
    while len(wine_items) >= 5:
        wine_items_sorted = sorted(wine_items, key=lambda item: item.price)
        discount += wine_items_sorted[0].price
        wine_items = wine_items[5:] 

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = total - discount + delivery
    
    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'discount': discount, 
    }

    return context
