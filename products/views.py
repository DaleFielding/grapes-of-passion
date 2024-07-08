from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def all_products(request):
    """ 
    Handle the display of all wine products,
    including sorting and search queries 
    """
    
    # Get all products and assign query/category to None to prevent errors
    products = Product.objects.all()
    query = None
    categories = None

    # Mapping to group certain categories
    grouped_categories = {
        'all-wine': ['red', 'white', 'rose'],
        'all-fortified-wine': ['port', 'sherry']
    }

    # If request contains category, filter products by category.
    # Handle grouped categories if specified in query parameters
    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']
            if category in grouped_categories:
                categories = grouped_categories[category]
            else:
                categories = [category]
                
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Check if a query searched.
        # If not show error message and redirect to products page.
        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
                
            # Adjust queries to search for name or type.
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        # If the discounted parameter is in the get request,
        # filter by including products that are not discounted
        if 'discounted' in request.GET:
            is_discounted = request.GET['discounted']
            products = products.exclude(discounted_price__isnull=True)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
