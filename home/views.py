from django.shortcuts import render, get_object_or_404
from products.models import Product 

def index(request):
    """ A view to return the index page """
    product = get_object_or_404(Product, pk=1)
    context = {
        'product': product,
    }
    return render(request, 'home/index.html', context)