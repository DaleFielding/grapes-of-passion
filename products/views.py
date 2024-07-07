from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """ Show all products, including sorting and search queries """
    # Get all products and set query to None initially to prevent query error

    products = Product.objects.all()
    query = None
    # Check if a query searched.
    # If not show error message and redirect to products page.
    if request.GET:
        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            # Adjust queries to search for name or type.
            queries = Q(name__icontains=query) | Q(type__icontains=query)
            products = products.filter(queries)
        # Check if category_ids are included in the get request,
        # then split the id's and filter the products by category_id
        if 'category_ids' in request.GET:
            category_ids = request.GET['category_ids'].split(',')
            products = products.filter(category_id__in=category_ids)

    context = {
        'products': products,
        'search_term': query,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
