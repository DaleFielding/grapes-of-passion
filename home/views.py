from django.shortcuts import render, get_object_or_404
from products.models import Product 


def index(request):
    """ A view to return the index page """

    # Recommended products to be displayed
    product1 = get_object_or_404(Product, pk=1)
    product2 = get_object_or_404(Product, pk=4)
    product3 = get_object_or_404(Product, pk=7)
    product4 = get_object_or_404(Product, pk=24)

    context = {
        'products': [product1, product2, product3, product4],
    }
    return render(request, 'home/index.html', context)