from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


# ---------- ALL PRODUCTS ---------- 
def all_products(request):
    """ 
    Handle the display of all wine products,
    including sorting and search queries
    """
    
    # Get all products and set default values for variables
    products = Product.objects.all()
    query = None
    categories = None
    is_discounted = False
    display_title = "No Products Found" 

    # Mapping to group certain categories
    grouped_categories = {
        'all-wine': ['red', 'white', 'rose'],
        'all-fortified-wine': ['port', 'sherry']
    }
# When get request contains 'category', filter products by category.
# Handle grouped categories if specified in query parameters
# Then assign intended title to display_title
    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']
            if category in grouped_categories:
                categories = grouped_categories[category]
                display_title = "All Wine" if category == 'all-wine' else "All Fortified Wine"
            else:
                categories = [category]
                display_title = Category.objects.get(name=category).name.capitalize()
                
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Handle query searched.
        # If not show error message and redirect to products page.
        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
                
            # Filter products by name or type)
            # Then assign query to display_title
            queries = Q(name__icontains=query) | Q(type__icontains=query)
            products = products.filter(queries)
            display_title = f"Results for '{query}'" 

        # If the discounted parameter is in the get request,
        # filter by including products that are not discounted
        # Then assign intended title to display_title
        if 'discounted' in request.GET:
            is_discounted = True
            products = products.exclude(discounted_price__isnull=True)
            display_title = "Discounted Products"  

    # context variables to be passed to the template
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'is_discounted': is_discounted,
        'display_title': display_title,
    }

    return render(request, 'products/products.html', context)


# ---------- PRODUCT DETAILS ---------- 
def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
