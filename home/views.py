from django.shortcuts import render, get_object_or_404
from products.models import Product  


def get_random_product(exclude_pks):
    """
    Get random product, excluding products with specified primary keys
    """
    products = Product.objects.exclude(pk__in=exclude_pks)
    if not products.exists():
        return None  
    return products.order_by('?').first()


def index(request):
    """
    Render index page with specified products or random replacements.
    """
    product_pks = [1, 4, 7, 24]
    products = []

    for pk in product_pks:
        try:
            product = get_object_or_404(Product, pk=pk)
        except:
            product = get_random_product([p.pk for p in products])
            if not product:
                continue
        products.append(product)

    context = {
        'products': products,
    }
    return render(request, 'home/index.html', context)